import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

HEADERS = { 'Accept-Language' : 'en-US', 'User-Agent': user_agent}


def price(search_item: str, iteration: int):
    new_search_item = search_item.replace(" ", "+")
    all_price: list = []

    for i in range(1, iteration + 1):
        url = f"https://www.amazon.com/s?k={new_search_item}&page={i}"
        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")
        price = soup.find_all('span', class_='a-price-whole')
        
        for j in range(0, len(price)):
            first = price[j].text

            dot_position = first.find(".")

            whole_price = first[:dot_position]
            # adding the value into an empty list
            all_price.append(whole_price)
        
    
    return all_price


def list_printer(ll: list):
    for item in ll:
        print(item)