import requests
import os
from dotenv import load_dotenv


load_dotenv()


SHOP = os.getenv("SHOPIFY_STORE")
CLIENT_ID = os.getenv("SHOPIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SHOPIFY_CLIENT_SECRET")


url = f"https://{SHOP}.myshopify.com/admin/oauth/access_token"


payload = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET
}


response = requests.post(
    url,
    data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }
)

response = requests.post(
    url,
    data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }
)


if response.status_code == 200:

    data = response.json()

    print("Access Token Generated Successfully")

    print(data["access_token"])

    print("Expires in:", data["expires_in"], "seconds")

else:

    print("Failed")
    print(response.status_code)
    print(response.text)