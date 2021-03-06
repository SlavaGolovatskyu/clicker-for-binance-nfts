import requests
from datetime import datetime
from keyboard import is_pressed


def getActiveMysteryBox(page=1, size=15) -> requests.Response:
    r = requests.get(f"https://www.binance.com/bapi/nft/v1/public/nft/mystery-box/list?page={page}&size={size}")
    return r
 

def parseActiveMysteryBoxList(req: requests.Response) -> list:
    nfts = []
    if req.status_code != 200:
        print('Ошибка парсинга. Попробуйте еще раз. Останавливаем скрипт.')
    else:
        r = req.json()
        for name in r['data']:
            # if status == 0 then nft active
            # else unactive
            if not name['status']:
                res = {
                    'Name': name['name'], 'Price': str(name['price']) + ' ' + name['currency'],
                    'ProductID': name['productId'], 'Start': name['startTime']
                }
                nfts.append(res)
    return nfts


def waitToStart(nfts: list):
    if list:
        old = int(str(nfts[0]['Start'])[:10])
        new = int(datetime.now().timestamp())

        while (old - new) >= 3:
            if is_pressed('ctrl+k'):
                print('Скрипт успешно остановлен')
                return
            new = int(datetime.now().timestamp())
            print(old - new, 'секунд осталось!')

# test = parseActiveMysteryBoxList(getActiveMysteryBox())

# old = str(test[0]['Start'])[:10]
# new = str(int(datetime.now().timestamp()))

# print(old, new, old==new)