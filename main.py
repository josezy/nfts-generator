from random import choice, choices
import json
import csv

import typer
from psd_tools import PSDImage

app = typer.Typer()


# random.choices(population=[['a','b'], ['b','a'], ['c','b']],weights=[0.2, 0.2, 0.6],k=10)

TRAITS = {
    "HANDs": {"choices": ["bald", "normal", None], "weights": [0.3, 0.3, 0.3]},
    "hats": {"choices": ["bald", "normal"], "weights": [0.5, 0.5]},
    "Body": {"choices": ["bald", "normal"], "weights": [0.5, 0.5]},
    "in mouth": {"choices": ["bald", "normal"], "weights": [0.5, 0.5]},
    "eye accessories": {"choices": ["bald", "normal"], "weights": [0.5, 0.5]},
    "face changes": {"choices": ["bald", "normal"], "weights": [0.5, 0.5]},
    "teeth": {"choices": ["bald", "normal"], "weights": [0.5, 0.5]},
    "backgrounds": {"choices": ["bald", "normal"], "weights": [0.5, 0.5]},
}

JSON_SCHEMA = {
    "name": "NAME_HERE",
    "symbol": "",
    "seller_fee_basis_points": 0,
    "image": "IMAGE_NAME",
    "properties": {
        "creators": [
            {"address": "5vdAeq93iynwZPGyj5QaSczQ9uYzvN4bRsJ4NySucZyB", "share": 100}
        ],
        "files": [{"uri": "image.png", "type": "image/png"}],
    },
}


def reset_visible(psd):
    for layer in psd:
        if layer.name in ["Mike bald shaved", "Mike normal hair and beard"]:
            layer.visible = False
        if layer.is_group():
            layer.visible = False
            layer.opacity = 0
            for child in layer:
                child.visible = False


def generate_nft_traits(traits):
    nft_traits = {}
    for trait, trait_data in traits.items():
        # typer.echo(
        #     f"{trait}: {choices(population=trait_data['choices'], weights=trait_data['weights'], k =1)}"
        # )
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


def generate_random_nft_image(filename):
    psd = PSDImage.open("mike_bisping.psd")
    use_bald = choice([True, False])
    for layer in psd:
        if layer.name == "mike bald" and use_bald:
            layer.visible = True
            # typer.echo("body: Mike bald")

        if layer.name == "mike normal" and not use_bald:
            layer.visible = True
            # typer.echo("body: Mike normal hair")

        if layer.is_group():
            layer.visible = True
            layer.opacity = 255
            # print(layer)
            child = choice(list(layer) + [None])
            if child:
                child.visible = True
            # typer.echo(f"{layer.name}: {child.name if child else None}")

    image = psd.composite(force=True, alpha=1.0, layer_filter=lambda l: l.visible)
    image.save(f"{filename}.png")

    json_data = JSON_SCHEMA.copy()
    json_data.update({"name": f"mike_nft_{filename}", "image": f"{filename}.png"})
    with open(f"{filename}.json", "w") as outfile:
        json.dump(json_data, outfile)


def main(
    count: int = 1,
    start_at: int = 0,
    generate: bool = False,
    read: bool = False,
    nft_file: str = None,
):

    nft_traits = []

    if read and nft_file:
        read_nft_traits(nft_file)
    elif read and not nft_file:
        raise ValueError('NFT file not provided')

    with typer.progressbar(range(count)) as progress:
        for i in progress:
            if generate:
                generate_random_nft_image(f"{i+start_at}")
            else:
                nft_traits.append(generate_nft_traits(TRAITS))

    if not generate and not read:
        with open("test.xls", "w") as f:
            # create the csv writer
            writer = csv.writer(f)

            # write the header
            writer.writerow(["id"] + [trait for trait in TRAITS])

            for count, traits in enumerate(nft_traits):
                writer.writerow([count + start_at] + [v[0] for v in traits.values()])

    typer.echo(f"Processed {count+1} images")


if __name__ == "__main__":
    app()
