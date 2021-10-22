import csv
import json
import time
import typer

from random import choices
from psd_tools import PSDImage

editionsPath = "./editions"


BACKGROUND_CHOICES = {
    "Count's Lair": 0.008,
    "Octagon": 0.012,
    "Union Jack": 0.008,
    "Solana": 0.04,
    "Black": 0.15,
    "Mustard": 0.07,
    "Green": 0.07,
    "Purple": 0.06,
    "Teal": 0.10,
    "Blue": 0.10,
    "Red": 0.10,
    "Blockasset": 0.032,
    None: 0.25,
}
BASE_CHOICES = {
    "Half Skull": 0.03,
    "Brains": 0.07,
    "Standard": 0.65,
    "Bald": 0.25,
    None: 0.0,
}
MOUTH_CHOICES = {
    "Union Jack Mouthguard": 0.06,
    "Cigarette": 0.09,
    "Cigar": 0.12,
    "Gold Mouthguard": 0.05,
    "Solana Mouthguard": 0.14,
    "Vampire Teeth": 0.04,
    "Missing Teeth": 0.07,
    "Diamond Grill": 0.02,
    "Falling Mouthguard": 0.07,
    "Gold Tooth": 0.04,
    None: 0.3,
}
FACE_CHOICES = {
    "Old Mike": 0.17,
    "Iron Mike": 0.10,
    "Black Eye": 0.0,
    "Stitches": 0.15,
    "Closed Eye": 0.0,
    "Bloody": 0.15,
    "Gold Terminator": 0.01,
    "Red Terminator": 0.02,
    None: 0.4,
}
EYES_CHOICES = {
    "Cyan Laser Eyes": 0.04,
    "Pink Laser Eyes": 0.09,
    "Green Laser Eyes": 0.09,
    "Red Laser Eyes": 0.09,
    "Yellow Laser Eyes": 0.09,
    "Orange Laser Eyes": 0.09,
    "Union Jack Laser Eyes": 0.02,
    "Bye Bye Eye": 0.002,
    "Hippie Shades": 0.05,
    "Solana Shades": 0.05,
    "Shades": 0.04,
    "Eye Patch": 0.005,
    "False Eye UK": 0.02,
    ### Missing layers ###
    # "Black Eye": 0.005,
    # "Closed Eye": 0.018,
    None: 0.3,
}
CLOTHING_CHOICES = {
    "Jiu Jitsu Robe ": 0.10,
    "Suit": 0.12,
    "Butcher": 0.02,
    "Quitters Never Win": 0.06,
    "Leather Jacket": 0.12,
    "Bloody Body": 0.11,
    "Inspirational Tattoo": 0.06,
    "Countdown": 0.06,
    "The Count": 0.01,
    "Soldier": 0.02,
    "Patriot": 0.002,
    "Punk Jacket": 0.018,
    None: 0.3,
}
HEAD_CHOICES = {
    "Butcher Hat": 0.02,
    "Elvis Hair": 0.06,
    "Announcer": 0.09,
    "DJ Mikey B": 0.038,
    "Red Training Headgear": 0.09,
    "Blue Training Headgear": 0.09,
    "Red Mohawk": 0.06,
    "Black Mohawk": 0.06,
    "Army Helmet ": 0.01,
    "Crown": 0.002,
    "Black Snapback": 0.09,
    "Red Snapback": 0.09,
    None: 0.3,
}
ACCESSORIES_CHOICES = {
    "Diamond Gloves": 0.008,
    "Gold Gloves": 0.03,
    "Solana Gloves": 0.05,
    "Blue Wrist Gloves": 0.09,
    "Red Wrist Gloves": 0.09,
    "Bloody Gloves": 0.09,
    "204 Belt": 0.016,
    "199 Belt": 0.016,
    "Microphone": 0.05,
    "Wraps": 0.09,
    "Bloody Wraps": 0.05,
    "Bare Fists": 0.09,
    "Knuckle Duster Spikes": 0.03,
    "Knuckle Duster": 0.05,
    None: 0.25,
}


TRAITS = {
    "BACKGROUND": BACKGROUND_CHOICES,
    "BASE": BASE_CHOICES,
    "MOUTH": MOUTH_CHOICES,
    "FACE": FACE_CHOICES,
    "EYES": EYES_CHOICES,
    "CLOTHING": CLOTHING_CHOICES,
    "HEAD": HEAD_CHOICES,
    "ACCESSORIES": ACCESSORIES_CHOICES,
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
        nft_traits[trait_name] = choices(
            population=list(trait_data.keys()), weights=list(trait_data.values()), k=1
        )

    return nft_traits


def read_nft_traits(file):
    with open(file, "rt") as f:
        data = csv.reader(f)
        # next(data, None)  # skip the headers
        for row in data:
            print(row)


def generate_candy_machine_edition(psd, traits):
    filename = traits["id"]
    typer.echo(f"Processing edition {filename}")

    for layer in psd[0]:
        if layer.name == traits["bodies"]:
            layer.visible = True

        if layer.name == "backgrounds":
            layer.visible = True
            backgrounds = [l for l in layer if l.name == "backgrounds 2"][0]
            backgrounds.visible = True
            background = [l for l in backgrounds if l.name == traits["backgrounds"]][0]
            background.visible = True

        if layer.name in traits:
            t_name = traits[layer.name]
            sublayer = [l for l in layer if l.name == t_name]
            if len(sublayer) == 1:
                layer.visible = True
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
            writer.writerow(["id"] + list(TRAITS.keys()))

            for count, traits in enumerate(nft_traits):
                writer.writerow([count + start_at] + [v[0] for v in traits.values()])

        typer.echo(f"Processed {count+1} images")


if __name__ == "__main__":
    typer.run(main)
