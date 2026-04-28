def lcs(X, Y):
    m, n = len(X), len(Y)
    
    # crear tabla
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    # llenar tabla
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp


def reconstruir_lcs(dp, X, Y):
    i, j = len(X), len(Y)
    res = []

    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            res.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(res))


# ===== EJECUCIÓN =====
X = "DEPLOY-PROD-08-01"
Y = "DEVELOP-DEBUG-01"

dp = lcs(X, Y)
lcs_str = reconstruir_lcs(dp, X, Y)

# imprimir tabla
print("TABLA DP:")
for fila in dp:
    print(fila)

print("\nLongitud LCS:", dp[len(X)][len(Y)])
print("LCS:", lcs_str)