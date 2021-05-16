
import pandas as pd
import pyupbit

# print(pyupbit.Upbit)

# # 모든 종목 코드 확인
# tickers = pyupbit.get_tickers()
# print(tickers)

# # KRW로 표기된 종목의 코드 확인
# tickers = pyupbit.get_tickers(fiat="KRW")
# print(tickers)

# 개별 가격 조회
price_KRW = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-DOGE"])

# print("\nBTC : {0:>10,} 원".format(int(price_KRW["KRW-BTC"]))) # 딕셔너리 type
# print("ETH : {0:>10,} 원".format(int(price_KRW["KRW-ETH"])))
# print("XRP : {0:>10,} 원".format(int(price_KRW["KRW-XRP"])))

# 아래와 같이 BTC로도 가격 조회가 가능함
# price_BTC = pyupbit.get_current_price("BTC-ETH")
# print("ETH : {} BTC\n".format(price_BTC))

# 참고 표준 출력 : https://wikidocs.net/20403

BTC_가격 = "BTC : " + format(int(price_KRW["KRW-BTC"]),",") + "원" 
ETH_가격 = "ETH : " + format(int(price_KRW["KRW-ETH"]),",") + "원"
XRP_가격 = "XRP : " + format(int(price_KRW["KRW-XRP"]),",") + "원"
DOGE_가격 = "DOGE : " + format(int(price_KRW["KRW-DOGE"]),",") + "원"

print(BTC_가격) 
print(ETH_가격) 
print(XRP_가격)
print(DOGE_가격)

price = BTC_가격 + "\n" + ETH_가격 + "\n" + XRP_가격 + "\n" + DOGE_가격

import telepot
token = "1409195797:AAFv2WmJOm3zjJUuDYKeKkdSLgTiwvV6Fg8" 
bot = telepot.Bot(token)
bot.sendMessage(chat_id = '@economystory', text = price)


