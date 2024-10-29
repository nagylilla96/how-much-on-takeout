import requests
import re
from config import TAZZ_COOKIE

def extract_remember_me(cookie_str):
    match = re.search(r'remember_me=([^;]+)', cookie_str)
    return match.group(1) if match else None

def fetch_tazz_orders():
    if not TAZZ_COOKIE:
        print("TAZZ_COOKIE is missing.")
        return 0.0, 0

    TAZZ_TOKEN = extract_remember_me(TAZZ_COOKIE)

    total_sum = 0.0
    order_count = 0
    headers = {"Authorization": TAZZ_TOKEN}
    url = "https://tapi.tazz.ro/orders/my-orders/0/10"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch Tazz data. Status code: {response.status_code}")
        return total_sum, order_count

    data = response.json()

    if data.get("success") and data.get("data"):
        orders = data["data"]["orders"]["items"]

        for order in orders:
            try:
                total_sum += float(order["totalPrice"])
                order_count += 1
            except (ValueError, KeyError) as e:
                print(f"Error parsing Tazz order price: {e}")

    return total_sum, order_count
