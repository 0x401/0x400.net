import requests
import re


def get_bing():
    resp = requests.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US')
    if resp.status_code == 200:
        return resp.json()['images'][0]['url']


def update_css(url):
    with open('style.css', 'r') as f:
        content = f.read()
        new = re.sub(r'https://www.bing.com(\/.+?)\s',  'https://www.bing.com'+url, content)
    with open('style.css', 'w') as f:
        f.write(new)


if __name__ == '__main__':
    url = get_bing()
    if url:
        update_css(url)