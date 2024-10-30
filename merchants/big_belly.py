import requests
import re
import io
from config import BASE_URL_BIG_BELLY, BIG_BELLY_AUTH_TOKEN

def extract_remember_me(cookie_str):
    match = re.search(r'remember_me=([^;]+)', cookie_str)
    return match.group(1) if match else None

def fetch_big_belly_orders():
    if not BIG_BELLY_AUTH_TOKEN:
        print("BIG_BELLY_AUTH_TOKEN is missing.")
        return 0.0, 0

    BIG_BELLY_TOKEN = extract_remember_me(BIG_BELLY_AUTH_TOKEN)

    total_sum = 0.0
    order_count = 0
    headers = {"Cookie": BIG_BELLY_AUTH_TOKEN}

    response = requests.get(BASE_URL_BIG_BELLY, headers=headers)
    with io.open("output.txt", mode="a", encoding="utf-8") as f:
        f.write(response.text)

    if response.status_code != 200:
        print(f"Failed to fetch Big Belly data. Status code: {response.status_code}")
        return total_sum, order_count

    try:
        data = response.json()
        print(data)
    except ValueError as e:
        print(f"Failed to parse Big Belly response: {e}")
        return total_sum, order_count

    if data.get("success") and data.get("data"):
        orders = data["data"]["orders"]["items"]

        for order in orders:
            try:
                total_sum += float(order["totalPrice"])
                order_count += 1
            except (ValueError, KeyError) as e:
                print(f"Error parsing Big Belly order price: {e}")

    return total_sum, order_count
