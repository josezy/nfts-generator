import csv
import json
import time
import typer

from random import choices
from psd_tools import PSDImage

editionsPath = './editions'


HANDs_CHOICES = ['diamond gloves', 'gold gloves copy', 'solana gloves ', 'clock ', 'blue wrist gloves', 'red wrist gloves', 'gloves with blood', '204 belt', '199 belt', 'holding mic copy', 'BUTCHER FULL SUIT', 'hand wraps ', 'hand wraps blood', 'Bare fists', 'knuckle duster spikes', 'knuckle duster ', None]
hats_CHOICES = ['butcher hat', 'elvis hair ', 'headphones copy', 'DJ headset ', 'headgear boxing  red', 'headgear boxing  blue', 'mohawk red', 'mohawk black', 'army helmet ', 'halo ', 'crown', 'snapback black', 'snapback red', None]
Body_CHOICES = ['jiu jitsu robe ', 'suit ', 'butcher', 't-shirt quitters never win', 'leather jacket copy', 'blood body ', 'body tattoo conceive believe', 'medal rockhold', 'clock ', 'Count full suit', 'army clothes copy', 'flag around back', 'punk jacket ', None]
in_mouth_CHOICES = ['cigarette copy', 'cigar copy', None]
eye_accessories_CHOICES = ['sunglasses 1', 'sunglasses 2 ', 'cyan', 'pink', 'green', 'red', 'yellow', 'orange', 'union jack laser', 'fallout eye left', 'fallout eye right', 'hippie sunglasses ', 'solana sunglasses ', 'eye patch', 'gold terminator ', 'red terminator ', 'false eye uk ', None]
face_changes_CHOICES = ['grey beard ', 'tyson tattoo', 'black eye', 'stitches', 'closed eye', 'blood copy', None]
teeth_CHOICES = ['UK', 'gold', 'solana', 'vampire', 'missing teeth', 'diamond grill', 'falling out mouth copy', 'gold tooth ', None]
background_CHOICES = ["Layer 293", "Layer 294", "Layer 295", "Layer 296", "Layer 297", "Layer 298", "Layer 299", "Layer 300"]
bodies_CHOICES = ["mike bald", "mike normal", "brains out", "half skeleton"]

TRAITS = {
  "HANDs": {
    "choices": HANDs_CHOICES,
    "weights": [1/len(HANDs_CHOICES) for _ in range(len(HANDs_CHOICES))]
  },
  "hats": {
    "choices": hats_CHOICES,
    "weights": [1/len(hats_CHOICES) for _ in range(len(hats_CHOICES))]
  },
  "Body": {
    "choices": Body_CHOICES,
    "weights": [1/len(Body_CHOICES) for _ in range(len(Body_CHOICES))]
  },
  "in mouth": {
    "choices": in_mouth_CHOICES,
    "weights": [1/len(in_mouth_CHOICES) for _ in range(len(in_mouth_CHOICES))]
  },
  "eye accessories": {
    "choices": eye_accessories_CHOICES,
    "weights": [1/len(eye_accessories_CHOICES) for _ in range(len(eye_accessories_CHOICES))]
  },
  "face changes": {
    "choices": face_changes_CHOICES,
    "weights": [1/len(face_changes_CHOICES) for _ in range(len(face_changes_CHOICES))]
  },
  "teeth": {
    "choices": teeth_CHOICES,
    "weights": [1/len(teeth_CHOICES) for _ in range(len(teeth_CHOICES))]
  },
  "backgrounds": {
    "choices": background_CHOICES,
    "weights": [1/len(background_CHOICES) for _ in range(len(background_CHOICES))]
  },
  "bodies": {
    "choices": bodies_CHOICES,
    "weights": [1/len(bodies_CHOICES) for _ in range(len(bodies_CHOICES))]
  },
}


def reset_visibility(psd):
    for layer in psd:
        if layer.is_group():
            reset_visibility(layer)
        else:
            layer.visible = False


def generate_nft_traits(traits):
    nft_traits = {}
    for trait, trait_data in traits.items():
        nft_traits[trait] = choices(
            population=trait_data["choices"], weights=trait_data["weights"], k=1
        )

    return nft_traits


def read_nft_traits(file):
    with open(file, "rt") as f:
        data = csv.reader(f)
        # next(data, None)  # skip the headers
        for row in data:
            print(row)


def generate_candy_machine_edition(psd, traits):
    filename = traits['id']
    typer.echo(f"Processing edition {filename}")

    for layer in psd[0]:
        if layer.name == traits['bodies']:
            layer.visible = True

        if layer.name == 'backgrounds':
            layer.visible = True
            backgrounds = [l for l in layer if l.name == 'backgrounds 2'][0]
            backgrounds.visible = True
            background = [l for l in backgrounds if l.name == traits['backgrounds']][0]
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
            "files": [{
                "uri": f"{filename}.png",
                "type": "image/png"
            }],
        },
    }
    with open(f"{editionsPath}/{filename}.json", "w") as outfile:
        json.dump(json_data, outfile)


def generate_editions(csv_filename, psd_filename):
    assert len(psd_filename) > 4 and psd_filename.split('.')[-1] == 'psd',\
        "Invalid or no PSD file provided"

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

            traits = {
                trait_name: row[i]
                for i, trait_name in enumerate(header)
            }

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
    psd_filename: str = 'base.psd',
    csv_filename: str = 'traits.csv',
):

    nft_traits = []

    if read and nft_file:
        read_nft_traits(nft_file)
    elif read and not nft_file:
        raise ValueError('NFT file not provided')

    if generate:
        generate_editions(csv_filename, psd_filename)

    else:
        with typer.progressbar(range(count)) as progress:
            for i in progress:
                nft_traits.append(generate_nft_traits(TRAITS))


    if not generate and not read:
        with open("traits.csv", "w") as f:
            # create the csv writer
            writer = csv.writer(f)

            # write the header
            writer.writerow(["id"] + [trait for trait in TRAITS])

            for count, traits in enumerate(nft_traits):
                writer.writerow([count + start_at] + [v[0] for v in traits.values()])

        typer.echo(f"Processed {count+1} images")


if __name__ == "__main__":
    typer.run(main)
