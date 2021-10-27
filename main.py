import csv
import json
import time
import typer

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
        None: 85,
        "Announcer": 7.5,
        "DJ Mikey B": 5,
        "Crown": 2.5,
    },
    "FACE": {
        None: 75,
        "Bloody": 15,
        "Red Terminator": 8,
        "Gold Terminator": 2,
    },
    "MOUTH": {
        None: 75,
        "Falling Mouthguard": 15,
        "Diamond Grill": 9.75,
        "Dosbrak Bandana": 0.25,
    },
    "EYES": {
        None: 94,
        "Wayfarers": 6,
    },
    "ACCESSORIES": {
        None: 49,
        "Gold Gloves": 24,
        "199 Belt": 19,
        "Microphone": 4.2,
        "Knuckle Duster Spikes": 3.3,
        "Diamond Gloves": 0.5,
    },
    "CLOTHING": {
        None: 50,
        "Bloody Body": 16,
        "Jiu Jitsu Robe": 15,
        "Suit": 7,
        "Punk Jacket": 7,
        "Patriot Flag": 2.5,
        "The Count": 2,
        "Astronaut": 0.5,
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

CATEGORIES = {
    "Common": [],
    "Uncommon": [],
    "Rare": [],
    "Super Rare": [],
    "Epic": [],
}


def reset_visibility(psd):
    for layer in psd:
        if layer.is_group():
            reset_visibility(layer)
        else:
            layer.visible = False


def generate_nft_traits(traits):
    nft_traits = {}
    for trait_name, trait_data in traits.items():
        weights = [weight / 100 for weight in trait_data.values()]
        nft_traits[trait_name] = choices(
            population=list(trait_data.keys()), weights=weights, k=1
        )

    return nft_traits


def read_nft_traits(file):
    with open(file, "rt") as f:
        data = csv.reader(f)
        # next(data, None)  # skip the headers
        for row in data:
            print(row)


def generate_candy_machine_edition(psd, traits):
    filename = traits["ID"]
    typer.echo(f"Processing edition {filename}")

    for layer in psd[0]:
        if layer.name.upper() not in traits:
            continue

        layer.visible = True
        sublayer = [l for l in layer if l.name == traits[layer.name.upper()]]
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


def generate_editions(csv_filename, psd_filename):
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

            # For testing generation of specific editions
            # if int(row[0]) not in [2, 3]:
            #     continue

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
):

    nft_traits = []

    if read and nft_file:
        read_nft_traits(nft_file)
    elif read and not nft_file:
        raise ValueError("NFT file not provided")

    if generate:
        generate_editions(csv_filename, psd_filename)

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
                writer.writerow([count + start_at] + [v[0] for v in traits.values()])

        typer.echo(f"Processed {count+1} images")


if __name__ == "__main__":
    typer.run(main)
