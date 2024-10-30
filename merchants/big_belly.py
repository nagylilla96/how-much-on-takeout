import requests
import re
# TODO: remove this, only added for testing
import io
from config import BASE_URL_BIG_BELLY, BIG_BELLY_AUTH_TOKEN
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def fetch_big_belly_orders():
    if not BIG_BELLY_AUTH_TOKEN:
        print("BIG_BELLY_AUTH_TOKEN is missing.")
        return 0.0, 0

    total_sum = 0.0
    order_count = 0
    headers = {"Cookie": BIG_BELLY_AUTH_TOKEN}

    response = requests.get(BASE_URL_BIG_BELLY, headers=headers)
    with io.open("output.txt", mode="a", encoding="utf-8") as f:
        f.write(response.text)

    if response.status_code != 200:
        print(f"Failed to fetch Big Belly data. Status code: {response.status_code}")
        return total_sum, order_count

    data = BeautifulSoup(response.text, 'html.parser')
    order_items = data.body.find('div', attrs={'id':'OrderItems'})

    if order_items:
        orders = order_items.text.split()
        
        index = 0
        for item in orders:
            index += 1
            if "Total" in item:
                total_sum += float(orders[index])
                order_count += 1

    return total_sum, order_count
