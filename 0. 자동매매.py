import pyupbit
잔고부족여부 = ""
매수알람 = ""
access_key = "t1l9CXgi8gZCMvT5kbfuJF2lwEFDx1H81ZRvdmSL"
secret_key = "qeixcAeaXJNZZG1prTXkJCqMKyhPb18dxV1FnlCi"
upbit = pyupbit.Upbit(access_key, secret_key)

# [매수 프로세스]
보유KRW = upbit.get_balance(ticker="KRW")         # 보유 KRW
if 보유KRW < 10000 : 
    잔액1만원미만알람 = "주문 잔액이 부족합니다."

else : 
    채결여부 = upbit.buy_market_order("KRW-BTC", 10000) #BTC 10,000원어치 시장가 매수
    print(채결여부["error"]["message"])
    잔고부족여부 = 채결여부["error"]["message"]
    매수알람 = "\nBTC를 매수하였습니다."
    print(매수알람)

# [잔고 조회]
보유KRW = upbit.get_balance(ticker="KRW")         # 보유 KRW
총매수금액 = upbit.get_amount('ALL')               # 총매수금액
비트수량 = upbit.get_balance(ticker="KRW-BTC")     # 비트코인 보유수량
이더수량 = upbit.get_balance(ticker="KRW-ETH")     # 비트코인 보유수량
리플수량 = upbit.get_balance(ticker="KRW-XRP")     # 리플 보유수량
도지수량 = upbit.get_balance(ticker="BTC-DOGE")     # 리플 보유수량

# [텔레그램 발송 문구작성]
잔액알람 = "(잔고 : {}원)\n".format(보유KRW)
총매수금액알람 = "\n총매수금액은 {}원 입니다.\n".format(총매수금액)
BTC수량알람 = "\n보유 BTC 수량은 {} 입니다.".format(비트수량)
이더수량알람 = "\n보유 ETH 수량은 {} 입니다.".format(이더수량)
리플수량알람 = "\n보유 XRP 수량은 {} 입니다.".format(리플수량)
도지수량알람 = "\n보유 DOGE 수량은 {} 입니다.".format(도지수량)
알람 = "[자동 매매 알람]\n" + 잔액1만원미만알람 + 잔고부족여부 + 잔액알람 + 매수알람 + 총매수금액알람 + BTC수량알람 + 이더수량알람 + 리플수량알람 + 도지수량알람
print(알람)

# [가격 조회]
price_KRW = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-DOGE"])

BTC_가격 = "BTC : " + format(int(price_KRW["KRW-BTC"]),",") + "원" 
ETH_가격 = "ETH : " + format(int(price_KRW["KRW-ETH"]),",") + "원"
XRP_가격 = "XRP : " + format(int(price_KRW["KRW-XRP"]),",") + "원"
DOGE_가격 = "DOGE : " + format(int(price_KRW["KRW-DOGE"]),",") + "원"

print(BTC_가격) 
print(ETH_가격) 
print(XRP_가격)
print(DOGE_가격)

price = "\n" + "\n" + "[업비트 시세]\n" + BTC_가격 + "\n" + ETH_가격 + "\n" + XRP_가격 + "\n" + DOGE_가격
알람 += price 

# [텔레그램 발송]
import telepot
token = "1409195797:AAFv2WmJOm3zjJUuDYKeKkdSLgTiwvV6Fg8" 
bot = telepot.Bot(token)
bot.sendMessage(chat_id = '@economystory', text = 알람)