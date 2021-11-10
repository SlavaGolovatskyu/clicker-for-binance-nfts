import requests

def getActiveMysteryBox(page=1, size=15) -> requests.Response:
    r = requests.get(f"https://www.binance.com/bapi/nft/v1/public/nft/mystery-box/list?page={page}&size={size}")
    return r


def parseActiveMysteryBoxList(req: requests.Response) -> list:
    r = req.json()
    nfts = []
    for name in r['data']:
        if not name['status']:
            res = {
                'Name': name['name'], 'Price': str(name['price']) + ' ' + str(name['currency']),
                'ProductID': name['productId'], 'Start': name['startTime']
            }
            nfts.append(res)
    return nfts

test = parseActiveMysteryBoxList(getActiveMysteryBox())

# old = str(test[0]['Start'])[:10]
# new = str(int(datetime.now().timestamp()))

# print(old, new, old==new)