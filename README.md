# How much on takeout

# Installation

1. Have Python 3 installed on your system
1. Clone this repo
1. Install a virtual environment with `python3 -m venv .venv/`
1. Activate virtualenv with `source .venv/bin/activate` on Linux or by running `.venv/Scripts/activate` on Windows
1. Install dependencies with `python3 -m pip install -r requirements.txt`
1. Run `cp .env.example .env`
1. Add the necessary authorization tokens in the `.env` file
1. Run the script with `python3 main.py`
1. Be shocked by how much money you spend

# How to get tokens/cookies
## Glovo
- URL: `https://glovoapp.com`
1. Open Glovo in your browser.
1. Open Developer Tools (usually accessible via F12 or Ctrl + Shift + I).
1. Log in with your account.
1. Go to the Network tab.
1. Find any request to `https://api.glovoapp.com/v3`.
1. Copy the Authorization token from the request headers.
1. Paste this token into the `.env` file as `GLOVO_AUTH_TOKEN`.

## Tazz
- URL: `https://tazz.ro`
1. Open Tazz in your browser.
1. Open Developer Tools and go to the Network tab.
1. Log in with your account.
1. Go to the Orders page.
1. Select the `orders` request that will be present in the network tab's list, and locate the Cookie header in the request headers.
1. Copy the entire Cookie header value.
1. Paste this cookie value into the `.env` file as `TAZZ_COOKIE`.

## Presto Pizza
- URL: `https://presto-pizza.ro`
1. Open Presto in your browser.
1. Open Developer Tools and go to the Network tab.
1. Log in with your account.
1. Find any request to `https://api.presto-pizza.ro/api/v2`.
1. Copy the UUID from the request headers (it will be used as the Authorization token).
1. Paste this UUID value into the `.env` file as `PRESTO_AUTH_UUID`.

## Bolt Food
- URL: `https://food.bolt.eu/en-US/history`
1. Open Bolt Food in your browser.
1. Open Developer Tools and go to the Network tab.
1. Log in with your account.
1. Select any request with the following format `https://deliveryuser.live.boltsvc.net/deliveryClient` and locate the Authorization token in the request headers.
1. Copy the Authorization token (formatted as Basic <token>).
1. Copy the Device Id parameter from the request.
1. Paste the token into the `.env` file as `BOLT_AUTH_TOKEN`.
1. Paste the device id into the `.env` file as `BOLT_DEVICE_ID`.

## Jerry's Pizza
- URL: `https://www.jerryspizza.ro/orders`
1. Open Jerry's Pizza in your browser, login if necesary
1. Open Developer Tools and go to the Network tab.
1. Go to "Istoric Comenzi"
1. Select any request with the following format `https://app.jerryspizza.ro/api2/index.php/order/all?id=...`
1. From the `Authorization` header copy the Bearer token
1. From the `X-Api-Key`  header copy the X-API-KEY
1. Paste the token into the `.env` file as `JERRYS_AUTH_TOKEN`.
1. Paste the key into the `.env` file as `JERRYS_X_API_KEY`.

## Big Belly
- URL: `https://www.bigbelly-cluj.ro`
1. Open Big Belly in your browser.
1. Log in with your account
1. Go to the Orders page.
1. Open Developer Tools and go to the Network tab.
1. Refresh the page.
1. Select the `contul-meu-comenzi` request that will be present in the network tab's list (it should be the first one after the refresh), and locate the Cookie header in the request headers.
1. Copy the entire Cookie header value.
1. Paste this cookie value into the `.env` file as `BIG_BELLY_COOKIE`.

# Special Thanks
- [nemesszili](https://github.com/nemesszili)
- [sorin25](https://github.com/sorin25)
