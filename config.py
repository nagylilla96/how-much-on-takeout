import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL_GLOVO = "https://api.glovoapp.com/v3/customer/orders-list?offset={0}&limit=100"
BASE_URL_PRESTO = "https://api.presto-pizza.ro/api/v2/get_history"
BASE_URL_TAZZ = "https://tapi.tazz.ro/orders/my-orders/0/1000000"
BASE_URL_BOLT = "https://deliveryuser.live.boltsvc.net/deliveryClient/getOrderHistory"
BASE_URL_JERRYS = "https://app.jerryspizza.ro/api2/index.php/order/all?id={0}"
BASE_URL_BIG_BELLY = "https://www.bigbelly-cluj.ro/contul-meu/contul-meu-comenzi"


GLOVO_AUTH_TOKEN = os.getenv("GLOVO_AUTH_TOKEN")
TAZZ_COOKIE = os.getenv("TAZZ_COOKIE")
PRESTO_AUTH_UUID = os.getenv("PRESTO_AUTH_UUID")
BOLT_AUTH_TOKEN = os.getenv("BOLT_AUTH_TOKEN")
BOLT_DEVICE_ID = os.getenv("BOLT_DEVICE_ID")
JERRYS_AUTH_TOKEN = os.getenv("JERRYS_AUTH_TOKEN")
JERRYS_X_API_KEY = os.getenv("JERRYS_X_API_KEY")
BIG_BELLY_AUTH_TOKEN = os.getenv("BIG_BELLY_AUTH_TOKEN")
