from time import time
import requests
from dotenv import load_dotenv
import os


class Mp3Downloader:
    def __init__(self, download_url, title, format):
        self.download_url = download_url
        self.title = title
        self.format = format

    def download(self, path=""):
        r = requests.get(self.download_url)
        download_path = os.path.join(path, f"{self.title}.{self.format}")
        with open(download_path, "wb") as download_file:
            download_file.write(r.content)


class Mp3Getter:
    main_url = "https://mp3-convert.org/get.php"

    def __init__(self, headers={"Referer": "https://mp3-convert.org"}, payload={"r": "hudar1255"}):
        self.payload = payload
        self.headers = headers
        self.session = requests.session()

    def get(self, link):
        self.payload["id"] = link.split("/")[-1]
        self.payload["t"] = int(time() * 1000)
        self.response = self.session.get(self.main_url, params=self.payload, headers=self.headers)
        self.data = self.response.json()
        return Mp3Downloader(
            self.data.get("download_url"),
            self.data.get("title"),
            self.data.get("format")
        )


def main():
    load_dotenv()
    link = os.environ.get("LINK")
    link_getter = Mp3Getter()
    downloader = link_getter.get(link)
    print(link_getter.data.get("title"))
    print(link_getter.data.get("download_url"))
    downloader.download(os.environ.get("DOWNLOAD_PATH"))


if __name__ == "__main__":
    main()