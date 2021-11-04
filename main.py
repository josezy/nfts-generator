import csv
import json
import time
import typer
import multiprocessing

from importlib import import_module
from typing import Optional
from random import choices
from psd_tools import PSDImage
from pathlib import Path


def reset_visibility(psd):
    for layer in psd:
        if layer.is_group():
            reset_visibility(layer)
        else:
            layer.visible = False

def set_deeper_visible(psd):
    for layer in psd:
        if layer.is_group():
            layer.visible = True
            set_deeper_visible(layer)
        else:
            layer.visible = True


def generate_nft_traits(traits, athlete_conditions):
    nft_traits = {}
    for trait_name, trait_data in traits.items():
        weights = [weight / 100 for weight in trait_data.values()]
        nft_traits[trait_name] = choices(
            population=list(trait_data.keys()), weights=weights, k=1
        )[0]

    return athlete_conditions(nft_traits)


def generate_candy_machine_edition(psd, traits, output_path, athlete_info, only_metadata):
    filename = traits["Edition".upper()]
    typer.echo(f"Processing edition {filename}")

    if not only_metadata:
        for layer in psd[0]:
            # Special Ali underwater case
            if layer.name == "Underwater folder" and traits["BASE"] == "Underwater":
                set_deeper_visible(layer)
                continue

            if layer.name.upper() not in traits:
                continue

            layer.visible = True

            if not layer.is_group():
                continue

            sublayer = [l for l in layer if l.name.strip() == traits[layer.name.upper()]]
            if len(sublayer) == 1:
                sublayer[0].visible = True
                # if sublayer is a group, set all sublayers to visible (special filters)
                if sublayer[0].is_group():
                    set_deeper_visible(sublayer[0])

        psd.composite(force=True).save(f"{output_path}/{filename}.png")

    json_data = {
        "name": "Blockasset Legends",
        "symbol": "LEGENDS",
        "seller_fee_basis_points": 7 * 100,
        "image": f"{filename}.png",
        "external_url": "https://blockasset.co/",
        "description": "Blockasset Verified Legends Collection by Dosbrak.",
        "properties": {
            "creators": [
                {
                    "address": "6SPSm4prbVn8LRAX41k81DnPaGDgV2YfExHQAjrep1tr",
                    "share": 100,
                },
            ],
            "files": [{"uri": f"{filename}.png", "type": "image/png"}],
        },
        "attributes": [
            {"trait_type": trait_name, "value": trait_value or "No trait"}
            for trait_name, trait_value in traits.items()
        ] + [
            {"trait_type": "LEGEND", "value": athlete_info.get('name')}
        ],
    }
    with open(f"{output_path}/{filename}.json", "w") as outfile:
        json.dump(json_data, outfile)


def generate_editions(csv_filename, psd_filename, output_path, athlete_info, only_metadata, traits_list=[]):
    assert (
        len(psd_filename) > 4 and psd_filename.split(".")[-1] == "psd"
    ), "Invalid or no PSD file provided"

    with open(csv_filename, "r") as f:

        reader = csv.reader(f)
        header = []
        start = time.time()
        for idx, row in enumerate(reader):
            if idx == 0:
                header = row
                continue

            if len(traits_list) > 0 and int(row[0]) not in traits_list:
                continue

            traits = {trait_name.upper(): row[i] for i, trait_name in enumerate(header)}

            psd = PSDImage.open(psd_filename)
            reset_visibility(psd)
            generate_candy_machine_edition(psd, traits, output_path, athlete_info, only_metadata)
        typer.echo(f"Elapsed time: {time.time() - start} secs")


def main(
    athlete: str,
    count: int = 1,
    generate: bool = False,
    only_metadata: bool = False,
    multiprocess: bool = False,
    trait_id: Optional[int] = None,
    trait_ids: str = "",
):
    typer.echo(f'Working with {athlete}')
    nft_traits = []

    _athlete = import_module(f'athletes.{athlete}')
    psd_filename = f"./athletes/{athlete}/base.psd"
    csv_filename = f"./athletes/{athlete}/traits.csv"
    output_path = f"./athletes/{athlete}/editions/"
    Path(output_path).mkdir(parents=True, exist_ok=True)

    if generate:
        typer.echo(f"Using {psd_filename} and {csv_filename}")
        if multiprocess:

            if trait_ids:
                l = list(map(int, trait_ids.split(",")))
                total_traits = len(trait_ids)
            else:
                with open(csv_filename) as fp:
                    total_traits = len(fp.readlines()) - 1
                l = list(range(total_traits))

            worker_pool = []
            worker_count = multiprocessing.cpu_count()

            splited = [l[i::worker_count] for i in range(worker_count)]

            for i in range(worker_count):

                if i >= total_traits:
                    break

                p = multiprocessing.Process(
                    target=generate_editions,
                    args=(csv_filename, psd_filename, output_path, _athlete.INFO, only_metadata),
                    kwargs={'traits_list': splited[i]}
                )
                p.start()
                worker_pool.append(p)

            for p in worker_pool:
                p.join()

        else:
            if trait_ids:
                t_list = list(map(int, trait_ids.split(",")))
            else:
                t_list = [] if trait_id is None else [trait_id]

            generate_editions(
                csv_filename,
                psd_filename,
                output_path,
                _athlete.INFO,
                only_metadata,
                traits_list=t_list
            )

    else:
        with typer.progressbar(range(count)) as progress:
            for _ in progress:
                new_trait = {}
                is_unique = False
                while not is_unique:
                    new_trait = generate_nft_traits(_athlete.TRAITS, _athlete.conditions)

                    duplicate_found = False
                    for existing_trait in nft_traits:
                        et_json = json.dumps(existing_trait)
                        nt_json = json.dumps(new_trait)
                        if et_json == nt_json:
                            duplicate_found = True
                            break

                    if not duplicate_found:
                        is_unique = True

                nft_traits.append(new_trait)

    if not generate:
        with open(csv_filename, "w") as f:
            # create the csv writer
            writer = csv.writer(f)

            # write the header
            writer.writerow(["Edition"] + list(_athlete.TRAITS.keys()))

            for count, traits in enumerate(nft_traits):
                writer.writerow([count] + list(traits.values()))

        typer.echo(f"Processed {count+1} images")


if __name__ == "__main__":
    typer.run(main)
