import requests
import sys

if len(sys.argv)!=2:
    sys.exit("Missing comman-line argument")
else:
    a=0
    try:
        a=float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
    
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = request.json()
    btc_price = data["bpi"]["USD"]["rate"]
    
    btc_price = btc_price.replace(",","")
    btc_price = float(btc_price)*a
    btc_price = "{:,.4f}".format(btc_price)
    
    print(f"${btc_price}")