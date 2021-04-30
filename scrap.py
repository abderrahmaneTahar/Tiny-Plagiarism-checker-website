import requests
from bs4 import BeautifulSoup


def search(phrase):
    phrase = '+'.join(phrase.split())
    url = 'https://www.google.com/search?q=' + phrase + '&ie=utf-8&oe=utf-8'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    return [link.find("a")["href"] for link in soup.find_all(class_="yuRUbf")[:2]]


def get_top_texts(phrase):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"}
    texts = []

    for link in search(phrase):
        print(link)
        text=""
        page = requests.get(link, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        for paragraph in soup.find_all("p"):
            text += paragraph.get_text()
        print(text)
        texts.append(text)
        print("*******************************************************************************************************")
    return texts


