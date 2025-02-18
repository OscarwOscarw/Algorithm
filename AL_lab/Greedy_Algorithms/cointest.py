import coin_changing

fewestcoin,fewestcoinlist = coin_changing.fewest_coins(18)

print(fewestcoin)
print(fewestcoinlist)
print("-------------------------------------------------------------------")
fewestcoin,fewestcoinlist,usedcoin = coin_changing.fewest_coins_list(29)
print(fewestcoin)
print(fewestcoinlist)
print(usedcoin)
print("-------------------------------------------------------------------")
fewestcoin = coin_changing.fewest_coins_dp(9)
print(fewestcoin)
print("-------------------------------------------------------------------")
fewestcoin_list = coin_changing.fewest_coins_list_dp(9)
print(fewestcoin_list)