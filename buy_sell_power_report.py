from zeep import Client

cl = Client("http://service.tsetmc.com/WebService/TsePublicV2.asmx?WSDL")

market_activity1 = cl.service.MarketActivityLast("ravandalgo.com","ravandalgo",1)#bourse
market_activity2 = cl.service.MarketActivityLast("ravandalgo.com","ravandalgo",2)#fara
# print('------------------------------------------------------------------------')
print('          orders values')
# print('------------------------------------------------------------------------')
print('traded value bourse : ' , f"{int(market_activity1['_value_1']['_value_1'][0]['MarketOverview']['MarketActivityQTotCap']):,}")
print('traded value farabourse : ' , f"{int(market_activity2['_value_1']['_value_1'][0]['MarketOverview']['MarketActivityQTotCap']):,}")
sum_activity = market_activity2['_value_1']['_value_1'][0]['MarketOverview']['MarketActivityQTotCap']+market_activity1['_value_1']['_value_1'][0]['MarketOverview']['MarketActivityQTotCap']
# print('------------------------------------------------------------------------')

print('total traded value of market today : ',f"{int(sum_activity/10000000000):,}",'B Toman ')
print('                                     ')
# print('                                       ')
# print('------------------------------------------------------------------------')
print('           buyer and seller power')
# print('------------------------------------------------------------------------')
best_limits1 = cl.service.BestLimitsAllIns("ravandalgo.com","ravandalgo",int(1))#bourse
best_limits2 = cl.service.BestLimitsAllIns("ravandalgo.com","ravandalgo",int(2))#farabourse
best_limits4 = cl.service.BestLimitsAllIns("ravandalgo.com","ravandalgo",int(4))#Payefara

total_buy_power = 0  # sum of ask_volume * ask_price of each row
total_sell_power = 0 # sum of bid_volume * bid_price pf each row

for best_limit in best_limits1['_value_1']['_value_1']:
	total_buy_power += best_limit['InstBestLimit']['QTitMeDem'] * best_limit['InstBestLimit']['PMeDem']
	total_sell_power += best_limit['InstBestLimit']['QTitMeOf'] * best_limit['InstBestLimit']['PMeOf']

for best_limit in best_limits2['_value_1']['_value_1']:
	total_buy_power += best_limit['InstBestLimit']['QTitMeDem'] * best_limit['InstBestLimit']['PMeDem']
	total_sell_power += best_limit['InstBestLimit']['QTitMeOf'] * best_limit['InstBestLimit']['PMeOf']

for best_limit in best_limits4['_value_1']['_value_1']:
	total_buy_power += best_limit['InstBestLimit']['QTitMeDem'] * best_limit['InstBestLimit']['PMeDem']
	total_sell_power += best_limit['InstBestLimit']['QTitMeOf'] * best_limit['InstBestLimit']['PMeOf']


print("5 first rows of buyers  : ", f'{int(total_buy_power/10000000000):,}', 'B Toman')
print("5 first rows of sellers  : ", f'{int(total_sell_power/10000000000):,}', 'B Toman')
print(" ")