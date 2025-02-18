def edit_dyn(s, t):
    les = len(s)
    let = len(t)
    
    dp = [[0] * (let + 1) for _ in range(les + 1)]
    a = [[0] * (let + 1) for _ in range(les + 1)]


    for i in range(les + 1):
        dp[i][0] = i
        a[i][0] = 1  
    for j in range(let + 1):
        dp[0][j] = j
        a[0][j] = 2 
    
    dp[0][0]=0

    for i in range(1, les + 1):
        for j in range(1, let + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                a[i][j] = 0  
            else:
                delet = dp[i - 1][j]
                insert = dp[i][j - 1]
                replace = dp[i - 1][j - 1]
                choose_op = min(replace, delet, insert)
                dp[i][j] = choose_op + 1
                
                if choose_op == replace:
                    a[i][j] = 1 
                elif choose_op == insert:
                    a[i][j] = 2  
                else:
                    a[i][j] = 3  
    print(a)  
    

    options = []
    i, j = les, let
    while i > 0 or j > 0:
        current = a[i][j]
        print(f"current: {current}, i: {i}, j: {j}")
        
        if current == 0:  
            options.append(0)
            i -= 1
            j -= 1
        elif current == 1: 
            options.append(1)
            i -= 1
            j -= 1
        elif current == 2: 
            options.append(2)
            j -= 1
        elif current == 3: 
            options.append(3)
            i -= 1

    options.reverse()  
    li_s = list(s)
    li_t = list(t)
    print("Operations:", options)
    for n in range(len(options)):
        option = options[n]
        if option == 3:
            li_t.insert(n, "-")
        if option == 2:
            li_s.insert(n,"-")

    print(" ".join(li_s))
    print(" ".join(li_t))
    return dp[les][let] 


