import urllib.request
import re


def download(url):
    print('Downloading:', url)
    try:
        html = urllib.request.open(url).read()
    except Exception as e:
        print('Download error:', e)
        html = None

    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        print(link)


base_url = 'http://www.dramaq.biz/'
jp_url = 'http://www.dramaq.biz/eigyou-buchou-kira-natsuko/'

with open('html.txt', 'w') as h:
    html = download(jp_url).decode('utf-8')
    if html:
        lines = html.split(' ')
        for line in lines:
            h.write(line)
    h.close()

