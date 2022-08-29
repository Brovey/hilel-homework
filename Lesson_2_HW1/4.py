import decimal
from decimal import Decimal, getcontext
rate = 40.70
uah = input("Введіть кількість гривень:")
getcontext().prec = len(uah) #len here to get an answer with 1 or 2 decimal digits as uah always longer then usd
usd = Decimal(uah)/Decimal(rate)
print("Станом на 25 серпня 2022 року це становить",usd,  "Долари США:(")