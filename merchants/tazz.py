import requests
from bs4 import BeautifulSoup
from config import TAZZ_COOKIE

def fetch_tazz_orders():
    if not TAZZ_COOKIE:
        print("TAZZ_COOKIE is missing.")
        return 0.0, 0
    
    total_sum = 0.0
    order_count = 0
    headers = {"Cookie": TAZZ_COOKIE}
    url = "https://tazz.ro/account/orders"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch Tazz data. Status code: {response.status_code}")
        return total_sum, order_count

    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all("div", class_="price")
    for price_div in prices:
        amount_text = price_div.get_text(strip=True).replace("Lei", "").replace(",", ".").strip()
        try:
            numeric_value = float(amount_text)
            total_sum += numeric_value
            order_count += 1
        except ValueError:
            print(f"Could not parse amount: {amount_text}")

    return total_sum, order_count
