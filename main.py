import json

import msgpack
import requests

try:
    url_latest = "https://api.matsurihi.me/mltd/v1/version/latest"
    latest_information = requests.get(url_latest).content.decode("utf-8")
    latest_information = json.loads(latest_information)
    version = latest_information["res"]["version"]
    indexName = latest_information["res"]["indexName"]

    url_Assets = f"https://td-assets.bn765.com/{version}/production/2018/Android/{indexName}"
    Assets = requests.get(url_Assets).content

    with open("manifest.json", mode="w") as manifest:
        json.dump(msgpack.unpackb(Assets), manifest, indent=4)

except Exception as e:
    print(e)

finally:
    print(f"current version: {version}")