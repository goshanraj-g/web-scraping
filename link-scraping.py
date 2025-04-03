import requests
from bs4 import BeautifulSoup


def linkScrape():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

if __name__ == '__main__':
    linkScrape()