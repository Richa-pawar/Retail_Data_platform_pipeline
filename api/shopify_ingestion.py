import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()


SHOP = os.getenv("SHOPIFY_STORE")
TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
API_VERSION = os.getenv("SHOPIFY_API_VERSION")


BASE_URL = (
    f"https://{SHOP}.myshopify.com/"
    f"admin/api/{API_VERSION}/graphql.json"
)


headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": TOKEN
}


def shopify_query(query):

    response = requests.post(
        BASE_URL,
        headers=headers,
        json={
            "query": query
        }
    )

    if response.status_code != 200:
        print(response.text)
        return None

    return response.json()



def save_json(filename, data):

    folder = "data/shopify"
    os.makedirs(folder, exist_ok=True)

    path = f"{folder}/{filename}"

    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4
        )

    print(f"Saved {path}")



# -------------------------
# Extract Products
# -------------------------

products_query = """

{
  products(first:50) {
    edges {
      node {
        id
        title
        status
        vendor
        productType

        variants(first:10){
          edges{
            node{
              id
              price
              inventoryQuantity
            }
          }
        }
      }
    }
  }
}

"""


products = shopify_query(products_query)

save_json(
    "products.json",
    products
)



# -------------------------
# Extract Customers
# -------------------------

customers_query = """

{
 customers(first:50){
   edges{
    node{
      id
      firstName
      lastName
      email
    }
   }
 }
}

"""


customers = shopify_query(customers_query)


save_json(
    "customers.json",
    customers
)



# -------------------------
# Extract Orders
# -------------------------

orders_query = """

{
 orders(first:50){
  edges{
   node{
    id
    name
    createdAt
    totalPriceSet{
      shopMoney{
        amount
        currencyCode
      }
    }
   }
  }
 }
}

"""


orders = shopify_query(orders_query)


save_json(
    "orders.json",
    orders
)

# -------------------------
# Extract Inventory
# -------------------------

inventory_query = """

{
 products(first:50){
  edges{
   node{
    id
    title

    variants(first:10){
     edges{
      node{
       id
       inventoryQuantity
      }
     }
    }
   }
  }
 }
}

"""


inventory = shopify_query(inventory_query)


save_json(
    "inventory.json",
    inventory
)

print("Shopify ingestion completed successfully")