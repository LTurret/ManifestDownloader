import json
import os

import argparse
import msgpack
import requests

version = None

parser = argparse.ArgumentParser(
    description="MLTD manifest download service."
)

parser.add_argument("-O", "--output_path", nargs=1, type=str, metavar="",
                    required=False,
                    default="./",
                    help="File output directory, If the directory is not found, create automatcally."
                )
parser.add_argument("-v", "--version", nargs=1, type=int, metavar="",
                    required=False,
                    help="Assign version, if version invalid, find leatest."
                )
group = parser.add_mutually_exclusive_group()
group.add_argument("--raw",
                  action="store_true",
                  help='Save ".data" format instead of ".json" as file.'
                )
opt = parser.parse_args()

def main(output_path, version, raw):

    save_raw = lambda bool: ".data" if (bool) else (".json")

    try:
        url_latest = "https://api.matsurihi.me/mltd/v1/version/latest"
        latest_information = requests.get(url_latest).content.decode("utf-8")
        latest_information = json.loads(latest_information)
        version = latest_information["res"]["version"]
        indexName = latest_information["res"]["indexName"]

        url_Assets = f"https://td-assets.bn765.com/{version}/production/2018/Android/{indexName}"
        Assets = requests.get(url_Assets).content
        
        file_path = f"{output_path[0]}/manifest{save_raw(raw)}"

        if not os.path.isdir(output_path[0]):
            os.mkdir(output_path[0])

        with open(file_path, mode="w") as manifest:
            json.dump(msgpack.unpackb(Assets), manifest, indent=4)

    except Exception as e:
        print(e)

    finally:
        print(f"Current resource version: {version}")
        print(f"Current indexName: {indexName}")
        print("Execution finish.")

if __name__ == "__main__":
    main(opt.output_path, opt.version, opt.raw)
