from os import link
from bs4 import BeautifulSoup

def get_pub_urls(html):
	soup = BeautifulSoup(html, 'html.parser')

	a_tags = soup.select('.row-fluid h3>a')

	# links = []

	# for tag in a_tags:
	# 	links.append(tag['href'])

	base_url = 'https://bnr.bg'

	links = [ base_url+tag['href'] for tag in a_tags]

	return links


