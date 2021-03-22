from lxml import etree
from io import StringIO


def raw_urls(html):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)
    links = tree.xpath('//a')
    for link in links:
        if 'href' not in link.attrib:
            continue
        url = link.attrib['href']
        title = ''.join(link.itertext()).strip()
        if not title:
            continue
        yield url, title


def unique_urls(html):
    seen = set()
    for url, title in raw_urls(html):
        if url in seen:
            continue
        seen.add(url)
        yield url, title
