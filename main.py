import json

import msgpack
import requests
import argparse

version = None

parser = argparse.ArgumentParser(
    description="MLTD manifest download service."
)

parser.add_argument("-O", "--output_path", nargs=1, type=str, metavar="",
                    required=False,
                    default="./",
                    help="File output directory/path, If the directory is not found, create automatcally."
                )
parser.add_argument("-v", "--version", nargs=1, type=int, metavar="",
                    required=False,
                    help="Assign version, if version invalid, find leatest."
                )

opt = parser.parse_args()

def main(output_path, version):
    try:
        url_latest = "https://api.matsurihi.me/mltd/v1/version/latest"
        latest_information = requests.get(url_latest).content.decode("utf-8")
        latest_information = json.loads(latest_information)
        version = latest_information["res"]["version"]
        indexName = latest_information["res"]["indexName"]

        url_Assets = f"https://td-assets.bn765.com/{version}/production/2018/Android/{indexName}"
        Assets = requests.get(url_Assets).content
        
        path = f"{output_path}/manifest.json"

        with open(path, mode="w") as manifest:
            json.dump(msgpack.unpackb(Assets), manifest, indent=4)

    except Exception as e:
        print(e)

    finally:
        print(f"Current version: {version}")
        print("Execution finish.")

if __name__ == "__main__":
    main(opt.output_path, version)
