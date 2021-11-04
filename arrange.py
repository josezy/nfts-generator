import os
import json
import typer

from pathlib import Path
from shutil import copyfile


def update_metadata(path, counter):
    with open(path, 'r+') as fp:
        md = json.load(fp)
        md["image"] = f"{counter}.png"
        md["properties"]["files"][0]['uri'] = md["image"]
        md["attributes"] = [
            {
                "trait_type": "EDITION",
                "value": str(counter),
            }
        ] + [trait for trait in md["attributes"] if trait["trait_type"] != "EDITION"]

        fp.seek(0)
        json.dump(md, fp)
        fp.truncate()

def main(
    athletes_dir: str,
    output_dir: str,
):
    typer.echo("Arranging assets")

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    athletes = ["lomu", "bisping", "rooney", "ovechkin", "ali"]

    counter = 0

    for athlete in athletes:
        for filename in os.listdir(f"{athletes_dir}/{athlete}/editions/"):
            if filename.endswith(".json"):
                fn_no_ext = os.path.splitext(filename)[0]
                aux_filename = f"{athletes_dir}/{athlete}/editions/{fn_no_ext}"
                copyfile(f"{aux_filename}.json", f"{output_dir}/{counter}.json")
                copyfile(f"{aux_filename}.png", f"{output_dir}/{counter}.png")
                update_metadata(f"{output_dir}/{counter}.json", counter)
                counter += 1


if __name__ == "__main__":
    typer.run(main)
