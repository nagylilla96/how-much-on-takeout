import requests
from config import BASE_URL_PRESTO, PRESTO_AUTH_UUID

def fetch_presto_orders():
    if not PRESTO_AUTH_UUID:
        print("PRESTO_AUTH_UUID is missing.")
        return 0.0, 0

    total_sum = 0.0
    order_count = 0
    headers = {"Authorization": PRESTO_AUTH_UUID}
    response = requests.get(BASE_URL_PRESTO, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch Presto data. Status code: {response.status_code}")
        return total_sum, order_count

    data = response.json()
    if "orders" in data:
        for order in data["orders"]:
            try:
                total_sum += float(order["total_price"])
                order_count += 1
            except (ValueError, KeyError) as e:
                print(f"Error parsing order price: {e}")

    return total_sum, order_count
