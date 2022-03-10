from lib import crawler
from lib import scraper

# from lib.crawler import get_html


url = 'https://bnr.bg/hristobotev/radioteatre/list'

html = crawler.get_html(url)
links = scraper.get_pub_urls(html)

print(links)
