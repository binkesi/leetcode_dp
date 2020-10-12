def cheapest_plane(n, flights, src, dst, k):
    dp = [[float("inf")] * n for _ in range(k+1)]
    # initial k=0 line.
    for i in flights:
        if i[0] == src:
            dp[0][i[1]] = i[2]
    # move one step forward and fill in the dp array, just keep the min value.
    for i in range(1, k+1):
        for j in range(n):
            if dp[i-1][j] != float("inf"):
                for f in flights:
                    if f[0] == j:
                        dp[i][f[1]] = min(dp[i][f[1]], dp[i-1][j]+f[2])
    min_value = dp[0][dst]
    for j in range(1, k+1):
        if dp[k][dst] < min_value:
            min_value = dp[k][dst]
    if min_value != float("inf"):
        return min_value
    else:
        return -1            
    
    
if __name__ == "__main__":
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    n = 3
    src = 0
    dst = 2
    k = 1
    print(cheapest_plane(n, flights, src, dst, k))