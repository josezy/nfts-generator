import csv
import json
import time
import typer
import multiprocessing

from typing import Optional
from random import choices
from psd_tools import PSDImage

editionsPath = "./editions"


TRAITS = {
    "BASE": {
        "Standard": 80,
        "Bald": 15,
        "Old Mike": 5,
    },
    "HEAD": {
        None: 54,
        "Sparring Headgear": 14,
        "Snapback": 13,
        "Announcer": 12,
        "DJ Mikey B": 6,
        "Crown": 1,
    },
    "FACE": {
        None: 68,
        "Bloody": 20,
        "Red Terminator": 10,
        "Gold Terminator": 2,
    },
    "MOUTH": {
        None: 72,
        "Cigar": 12,
        "Falling Mouthguard": 11,
        "Diamond Grill": 4.75,
        "Dosbrak Bandana": 0.25,
    },
    "EYES": {
        None: 62,
        "Wayfarers": 18,
        "Bruised Eye": 13,
        "Laser Eyes": 7,
    },
    "ACCESSORIES": {
        None: 15,
        "Bare Fists": 15,
        "Gloves": 14,
        "Bloody Wraps": 12,
        "Bloody Gloves": 11,
        "Microphone": 10,
        "SOL Gloves": 8,
        "Gold Gloves": 7,
        "199 Belt": 4.5,
        "Knuckle Duster Spikes": 2.5,
        "Diamond Gloves": 1,
    },
    "CLOTHING": {
        None: 20,
        "Bloody Body": 19,
        "Jiu Jitsu Robe": 14,
        "Suit": 12,
        "Tattoo": 11,
        "Punk Jacket": 10,
        "Butcher": 6,
        "Patriot Flag": 5,
        "The Count": 2,
        "Astronaut": 1,
    },
    "BACKGROUND": {
        "Teal": 20,
        "Black": 20,
        "Red": 20,
        "Purple": 15,
        "Mustard": 15,
        "Blockasset": 5,
        "Octagon": 4.2,
        "Count's Lair": 0.8,
    },
}


def reset_visibility(psd):
    for layer in psd:
        if layer.is_group():
            reset_visibility(layer)
        else:
            layer.visible = False


def review_and_fix_special_cases(nft_traits):

    # 'Microphone' trait should only show with 'Suit' trait
    if nft_traits['ACCESSORIES'] == 'Microphone':
        nft_traits['CLOTHING'] = 'Suit'

    # 'Wayfarer' trait should not show with 'Sparring Headgear' trait
    if nft_traits['HEAD'] == 'Sparring Headgear':
        nft_traits['EYES'] = None

    # 'Astronaut' should show with 'Standard' base trait only please
    if nft_traits['CLOTHING'] == 'Astronaut':
        nft_traits['BASE'] = 'Standard'

    # 'Dosbrak Bandana' trait should not show with 'Sparring Headgear' trait
    if nft_traits['HEAD'] == 'Sparring Headgear':
        nft_traits['MOUTH'] = 'Diamond Grill'

    return nft_traits

def generate_nft_traits(traits):
    nft_traits = {}
    for trait_name, trait_data in traits.items():
        weights = [weight / 100 for weight in trait_data.values()]
        nft_traits[trait_name] = choices(
            population=list(trait_data.keys()), weights=weights, k=1
        )[0]

    return review_and_fix_special_cases(nft_traits)


def read_nft_traits(file):
    with open(file, "rt") as f:
        data = csv.reader(f)
        # next(data, None)  # skip the headers
        for row in data:
            print(row)


def generate_candy_machine_edition(psd, traits):
    filename = traits["ID"]
    typer.echo(f"Processing edition {filename}")

    # Signature
    psd[1].visible = True

    for layer in psd[0]:
        if layer.name.upper() not in traits:
            continue

        layer.visible = True
        sublayer = [l for l in layer if l.name.strip() == traits[layer.name.upper()]]
        if len(sublayer) == 1:
            sublayer[0].visible = True

    psd.composite(force=True).save(f"{editionsPath}/{filename}.png")

    json_data = {
        "name": f"Michael Bisping Ed. {filename}",
        "symbol": "",
        "seller_fee_basis_points": 0,
        "image": f"{filename}.png",
        "properties": {
            "creators": [
                {
                    "address": "6Ai61gQBy4uRahRpkNm6ZbVyvUjGtBgm1ns9qu4xAL5N",
                    "share": 50,
                },
                {
                    "address": "6uDvPTDPgRaCBuSK5Jq531TugMEXJXm8APhzca3T2KuR",
                    "share": 50,
                },
            ],
            "files": [{"uri": f"{filename}.png", "type": "image/png"}],
        },
        "attributes": [
            {"trait_type": trait_name, "value": trait_value}
            for trait_name, trait_value in traits.items()
        ],
    }
    with open(f"{editionsPath}/{filename}.json", "w") as outfile:
        json.dump(json_data, outfile)


def generate_editions(csv_filename, psd_filename, traits_list=[]):
    assert (
        len(psd_filename) > 4 and psd_filename.split(".")[-1] == "psd"
    ), "Invalid or no PSD file provided"

    with open(csv_filename, "r") as f:
        typer.echo(f"Using {psd_filename} and {csv_filename}")

        reader = csv.reader(f)
        header = []
        start = time.time()
        for idx, row in enumerate(reader):
            if idx == 0:
                header = row
                continue

            if len(traits_list) > 0 and int(row[0]) not in traits_list:
                continue

            traits = {trait_name: row[i] for i, trait_name in enumerate(header)}

            psd = PSDImage.open(psd_filename)
            reset_visibility(psd)
            generate_candy_machine_edition(psd, traits)
        typer.echo(f"Elapsed time: {time.time() - start} secs")


def main(
    count: int = 1,
    start_at: int = 0,
    generate: bool = False,
    read: bool = False,
    nft_file: str = None,
    psd_filename: str = "base.psd",
    csv_filename: str = "traits.csv",
    multiprocess: bool = False,
    trait_id: Optional[int] = None,
):

    nft_traits = []

    if read and nft_file:
        read_nft_traits(nft_file)
    elif read and not nft_file:
        raise ValueError("NFT file not provided")

    if generate:
        if multiprocess:

            with open(csv_filename) as fp:
                total_traits = len(fp.readlines()) - 1

            worker_pool = []
            worker_count = multiprocessing.cpu_count()

            l = list(range(total_traits))
            splited = [l[i::worker_count] for i in range(worker_count)]

            for i in range(worker_count):

                if i >= total_traits:
                    break

                p = multiprocessing.Process(
                    target=generate_editions,
                    args=(csv_filename, psd_filename),
                    kwargs={'traits_list': splited[i]}
                )
                p.start()
                worker_pool.append(p)

            for p in worker_pool:
                p.join()

        else:
            generate_editions(csv_filename, psd_filename, traits_list=[] if trait_id is None else [trait_id])

    else:
        with typer.progressbar(range(count)) as progress:
            for _ in progress:
                nft_traits.append(generate_nft_traits(TRAITS))

    if not generate and not read:
        with open(csv_filename, "w") as f:
            # create the csv writer
            writer = csv.writer(f)

            # write the header
            writer.writerow(["ID"] + list(TRAITS.keys()))

            for count, traits in enumerate(nft_traits):
                writer.writerow([count + start_at] + list(traits.values()))

        typer.echo(f"Processed {count+1} images")


if __name__ == "__main__":
    typer.run(main)
