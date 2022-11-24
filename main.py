import requests
from bs4 import BeautifulSoup
from my_func import *


search_topic = input("Enter your search topic: ")
how_many_pages: int = int(input("How many pages you wanna check?: "))

print("\n\nPlease wait...\n\n")
price: list = price(search_topic, how_many_pages)

print("Total item:", len(price), ". See below: \n")
list_printer(price)


print("\n")
cfjdgcfuj = input("Hit enter to close....")




