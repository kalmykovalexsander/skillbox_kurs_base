import time
from urllib.parse import urlsplit, urljoin

import requests
from urllib.request import urlopen
from html.parser import HTMLParser
from html.entities import name2codepoint

sites = [
    'https://www.fl.ru',
    'https://kubzan.ru/',
    'https://www.gosuslugi.ru/',
    'https://www.ya.ru',
    # 'https://www.yaplakal.ru/',
    'https://www.rbc.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    # 'https://kwork.ru',
    'https://work-zilla.com/',
    'https://iklife.ru/udalennaya-rabota-i-frilans/poisk-raboty/vse-samye-luchshie-sajty-i-birzhi-v-internete.html',
]

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


class LinkExtractor(HTMLParser):

    def __init__(self, base_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = base_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag not in ('link', 'script', ):
            return
        attrs = dict(attrs)
        if tag == 'link':
            if 'rel' in attrs and attrs['rel'] == 'stylesheet':
                link = self._refine(attrs['href'])
                self.links.append(link)
        elif tag == 'script':
            if 'src' in attrs:
                link = self._refine(attrs['src'])
                self.links.append(link)

    def _refine(self, link):
        return urljoin(self.base_url, link)

class PageSize:

    def __init__(self, url):
        self.url = url
        self.total_bytes = 0

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(url=self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        extractor = LinkExtractor(base_url=self.url)
        extractor.feed(html_data)
        for link in extractor.links:
            extra_data = self._get_html(url=link)
            if extra_data:
               self.total_bytes += len(extra_data)


    def _get_html(self, url):
        try:
            print(f'go {url}...')
            res = requests.get(url)
        except Exception as exc:
            print(exc)
        else:
            return res.text

@time_track
def main():
    sizers = [PageSize(url=url) for url in sites]

    for sizer in sizers:
        sizer.run()
    for sizer in sizers:
        print(f'For url {sizer.url} need download {sizer.total_bytes // 1024} KB')


if __name__ == '__main__':
    main()