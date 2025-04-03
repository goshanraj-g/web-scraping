import requests
from bs4 import BeautifulSoup
from googlesearch import search

def scrape():
    query=""

    for result in search(query, num_results=10):
        url = result
        print(f"Scraping: {url}")

        try: 
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.select_one('h1').text if soup.select_one('h1') else "No <h1> found"
            text = soup.select_one('p').text if soup.select_one('p') else "No <p> found"
            link = soup.select_one('a').get('href') if soup.select_one('a') else "No <a> found"

            
            print("Title:", title)
            print("Snippet:", text)
            print("First link:", link)

        except Exception as e:
            print(f"There was an error scraping {url}: {e}")

if __name__ == '__main__':
    scrape()


