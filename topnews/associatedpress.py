import re
import requests
from topnews.utils import unique_urls


def urls(html):
    for url, title in unique_urls(html):
        if not re.match(r'^/article/', url):
            continue
        yield f'https://apnews.com{url}', title


def fetch():
    res = requests.get('https://apnews.com/hub/ap-top-news')
    for url, title in urls(res.text):
        print(url)
        print(title)


if __name__ == '__main__':
    fetch()
