import pyupbit as pb


# print(pb.Upbit)
# # ticker 조회  fiat parameter 을 이용해 원화로 거래되는 ticker만 조회할 수 있다.
# ticker = pb.get_tickers(fiat="KRW")
# # print(ticker)
# # 비트코인의 현재가를 조회
# BTC_Price = pb.get_current_price("KRW-BTC")
# # print(BTC_Price)
# # 해당코인의과거데이터를 조회한다. count 로 원하는 만큼 가져올 수 있다.
# # df = pb.get_ohlcv("KRW-BTC")
# df = pb.get_ohlcv("KRW-BTC", count = 5)
# # print(df)
# # 비트코인 호가창 조회

# order_book = pb.get_orderbook("KRW-BTC")
# bids_ask = order_book[0]['orderbook_units']
# print(bids_ask)

# 잔고 조회하기
f = open("Key.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
print(access,"\n", secret)
upbit = pb.Upbit(access,secret)
balance = upbit.get_balances()
print(balance)

