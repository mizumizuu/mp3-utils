from time import time
from requests_html import HTMLSession
import os


class Mp3Downloader:
    def __init__(self, download_url, title, session=HTMLSession()):
        self.download_url = download_url
        self.title = title
        self.session = session

    def download(self, path=""):
        r = self.session.get(self.download_url)
        download_path = os.path.join(path, f"{self.title}.mp3")
        with open(download_path, "wb") as download_file:
            download_file.write(r.content)


class Mp3Getter:
    main_url = "https://mp3-convert.org/get.php"

    def __init__(self, headers={"Referer": "https://mp3-convert.org"}, payload={"r": "hudar1255"}):
        self.payload = payload
        self.headers = headers
        self.session = HTMLSession()

    def get_title(self, link):
        r = self.session.get(link)
        title = r.html.find("title", first=True).text
        title = title.split(" - YouTube")[0]
        return title

    def get(self, link):
        self.payload["id"] = link.split("/")[-1]
        self.payload["t"] = int(time() * 1000)
        self.response = self.session.get(self.main_url, params=self.payload, headers=self.headers)
        self.data = self.response.json()
        self.data["title"] = self.get_title(link)
        return Mp3Downloader(
            self.data.get("download_url"),
            self.data.get("title"),
            self.session
        )

def main():
    link = input("link: ")
    getter = Mp3Getter()
    downloader = getter.get(link)
    downloader.download()

if __name__ == "__main__":
    main()
