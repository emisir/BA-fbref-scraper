import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
session = requests.Session()

def scrape_fbref(url):
    response = session.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    

main_url = 'https://fbref.com/en/comps/20/2023-2024/stats/2023-2024-Bundesliga-Stats'
scrape_fbref(main_url)
