import sys
import requests

try:
    n = float(sys.argv[1])
except (ValueError,IndexError):
    sys.exit("Missing command-line argument")
    
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=f0f9b14fa576558d198dd76b2e1a59906c2fdb9e2bff9ad092196e7230b908c5")
    response.raise_for_status()
except requests.RequestException:
    sys.exit()
    
content = response.json()

price = content["data"]["priceUsd"]
price = float(price)

total = price * n
#print(price)
print(f"${total:,.4f}")
