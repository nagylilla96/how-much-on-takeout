import requests
from config import BASE_URL_BOLT, BOLT_AUTH_TOKEN, BOLT_DEVICE_ID

def fetch_bolt_food_orders():
    if not BOLT_AUTH_TOKEN:
        print("BOLT_AUTH_TOKEN is missing.")
        return 0.0, 0

    total_sum = 0.0
    order_count = 0

    headers = {
        "Authorization": "Basic " + BOLT_AUTH_TOKEN,
        "Host": "deliveryuser.live.boltsvc.net",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }

    params = {
        "version": "FW.1.76",
        "language": "ro-RO",
        "device_name": "web",
        "device_os_version": "web",
        "deviceId": BOLT_DEVICE_ID,
        "deviceType": "web"
    }

    response = requests.get(BASE_URL_BOLT, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch Bolt Food data. Status code: {response.status_code}")
        return total_sum, order_count

    data = response.json()

    orders = data.get("data", {}).get("orders", [])
    for order in orders:
        try:
            total_sum += float(order["price"]["value"])
            order_count += 1
        except (ValueError, KeyError) as e:
            print(f"Error parsing Bolt Food order price: {e}")

    return total_sum, order_count
