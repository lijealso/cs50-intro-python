import requests
import sys

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
try:
    bitcoin = float(sys.argv[1])
except (requests.RequestException, ValueError):
    print("Command-line argument is not a number")
    pass
else:
    resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = resp.json()

rateUSD = bitcoin * float(o["bpi"]["USD"]["rate"].replace(',', ''))
format_float = "{:.4f}".format(rateUSD)
print("$" + str(format_float)[0:2] + ',' + str(format_float)[2:])