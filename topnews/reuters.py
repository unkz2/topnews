import re
import requests
from topnews.utils import unique_urls


def urls(html):
    for url, title in unique_urls(html):
        if not re.match(r'^/article/', url):
            continue
        if 'reuters-editorial-leadership' in url:
            continue
        yield f'https://www.reuters.com{url}', title


def fetch():
    res = requests.get('https://www.reuters.com/news/archive/newsOne')
    for url, title in urls(res.text):
        print(url)
        print(title)


if __name__ == '__main__':
    fetch()
