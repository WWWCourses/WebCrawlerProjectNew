import requests

def get_html(url):
	r = requests.get(url)

	if r.ok:
		html = r.text
		return html



