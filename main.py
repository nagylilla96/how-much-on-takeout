import requests
import re

BASE_URL = "https://api.glovoapp.com/v3/customer/orders-list?offset={0}&limit=100"
AUTH_TOKEN = ""

if not AUTH_TOKEN:
    raise ValueError("Authorization token is missing. Please set 'AUTH_TOKEN'")

headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

offset = 0
total_sum = 0.0
order_count = 0

def process_orders(orders):
    global total_sum, order_count
    for order in orders:
        footer_left_data = order["footer"]["left"]["data"]
        
        amount = re.search(r"([\d,]+)\sRON", footer_left_data)
        if amount:
            numeric_value = float(amount.group(1).replace(",", "."))
            total_sum += numeric_value
            order_count += 1

def fetch_orders():
    global offset

    while True:
        url = BASE_URL.format(offset)
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            break

        data = response.json()

        if "orders" in data:
            process_orders(data["orders"])
        else:
            print("No 'orders' key found in response.")
            break

        next_page = data.get("pagination", {}).get("next")
        if not next_page:
            break
        else:
            offset = next_page.get("offset", offset)

def main():
    fetch_orders()
    average_order_value = total_sum / order_count if order_count > 0 else 0
    print(f"Total sum: {total_sum:.2f} RON")
    print(f"Total number of orders: {order_count}")
    print(f"Average order value: {average_order_value:.2f} RON")

if __name__ == "__main__":
    main()
