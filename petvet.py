# Post de Rappi

import re
import requests
import json
# url = "https://services.grability.rappi.com/api/cpgs-integration/datasets"
# datos = '0779e534d934e8e51f4c.json'


# headers = {
#    'Content-Type': 'application/json',
#    "api_key":"6bc37261-7615-47c0-b6d8-91c23b747cea"
# }

# param = {"records":[{"id": "321231","store_id": "32132","ean": 700123,"name": "XXXXXXXXX","trademark": "X Brand","price": 313212,"discount_price": 1,"stock": 321,"sale_type": "U","is_available": "True"}]}
# param2 = json.dumps(param)
# response = requests.request("POST", url, headers=headers, data=datos)



# print(response.status_code)

# Get con Api de Bsale
url = "https://api.bsale.cl/v1/products.json"
datos = '6cc26c07ec782ca618620c30c1e7afdeab5b165a.json'

headers = {
   'Content-Type': 'application/json',
   "access_token":"6cc26c07ec782ca618620c30c1e7afdeab5b165a"
}

# response = requests.request("GET", url, headers=headers)
response = requests.get(url=url, headers=headers)
# print(response.status_code)
print(response.content)
json_response = response.json()




