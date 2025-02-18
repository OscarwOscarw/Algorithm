# File: coin_changing.py
# COIN CHANGING PROBLEMS.

import sys
sys.setrecursionlimit(10000)

# Some coin systems:


lecture_coins = [1,6,8]    

sterling_coins = [1,2,5,10,20,50,100,200]


# Problem (1): Minimum number of coins (as in Lecture 18).

c_list = lecture_coins  # global variable, can set as desired



# Plain recursive implementation.
# fewest_coins should be implemented recursively, returning just smallest number of coins.


def fewest_coins(v):
    C = [0]*(v+1)
    C[1] = 1
    k = len(c_list)
    w = 2
    if v == 0:      
        return 0
    if v == 1:
        return 1
    else:
        for w in range(2,v+1):
            C[w] = float('inf')
            for i in range(k):
                if c_list[i] <= w and C[w-c_list[i]]+1<C[w]:
                    C[w] = C[w-c_list[i]]+1
    
    return C[v],C





# slightly different method which returns a list of actual coins (which constitute a 
# minimum-sized solution).

def fewest_coins_list(v):
    C = [0]*(v+1)
    C[1] = 1
    k = len(c_list)
    P = [0]*(v+1)
    P[1]=1
    coinprocess = []
    usedcoin = []
    w = 2
    if v == 0:      
        return 0
    if v == 1:
        return 1
    else:
        for w in range(2,v+1):
            C[w] = float('inf')
            for i in range(k):
                if c_list[i] <= w and C[w-c_list[i]]+1<C[w]:
                    C[w] = C[w-c_list[i]]+1
                    coinprocess.append(w-c_list[i])
                    P[w] = c_list[i]
    process = v
    for n in range(C[v]):
        coin = P[process]
        usedcoin.append(coin)
        process = process - coin


        

    return C[v],C,usedcoin


 

# Memoization operation, exactly as in our lecture:

def memoize(f):
    memo = {}
    def check(v):
        if v not in memo:
            memo[v] = f(v)
        return memo[v]
    return check

# memoize : (int->int) -> (int->int)
# f : int->int,  check : int->int

# To get the optimization of the recursion:

#   fewest_coins = memoize(fewest_coins)
#   fewest_coins_list = memoize(fewest_coins_list)

# NB. Can't change c_list after doing this!
# We would need to reload the file within the Python interpreter to use with new c_list.

# You should also implement and experiment with a dynamic programming solution,
# as given towards the end of slide-set 18.


def fewest_coins_dp(v):
    memoized_fewest_coins = memoize(fewest_coins) 
    return memoized_fewest_coins(v)

    

def fewest_coins_list_dp(v):
    memoize_fewest_coins_list = memoize(fewest_coins_list)
    return memoize_fewest_coins_list(v)
