from bs4 import BeautifulSoup
from googlesearch import search
import os
import requests
import urllib


def Wikipedia():

    site = "en.wikipedia.org/"
    genre = "Series"

    for movie in files:
        try:
            if os.path.exists(f"{movie}\\"):
                for item in os.listdir(f"{movie}\\"):
                    item = item.split(".")
                    if ("jpg" in item) or ("png" in item) or ("jpeg" in item):
                        break
                else:
                    query = site + movie + genre
                    result = search(query, "com", stop=3)  # result of search
                    for url in result:
                        if site in url:
                            r = requests.get(url)
                            soup = BeautifulSoup(r.text, "html5lib")
                            selected = soup.find("a", class_="image")
                            selected = selected.find("img")
                            img_url = selected.attrs["src"]
                            img_url = "https:" + img_url
                            img_format = img_url.split('.')[-1]
                            urllib.request.urlretrieve(
                                img_url, f"{movie}\\{movie}.{img_format}")  # saving image
                            print(
                                f"""---------------------------
            name: {movie}\nurl: {url}\nimage url: {img_url}\nstatus:{"✅Ok✅"}
        ---------------------------""")
                            break
        except AttributeError:
            print(
                f"""---------------------------
    name: {movie}\nurl: {url}\nimage url: {img_url}\nstatus:{"❌Error❌"}
---------------------------""")
            continue


if __name__ == "__main__":
    files = os.listdir()
    Wikipedia()
