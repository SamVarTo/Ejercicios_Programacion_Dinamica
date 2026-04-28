def knapsack():
    val = [7, 9, 4, 6]
    wt = [3, 5, 2, 4]
    W = 10
    n = len(val)

    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               val[i-1] + dp[i-1][w-wt[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    # imprimir tabla
    for fila in dp:
        print(fila)

    print("Resultado:", dp[n][W])


knapsack()