# leetcode 1416ms
def cheapest_plane(n, flights, src, dst, k):
    dp = [[float("inf")] * n for _ in range(k+1)]
    # initial k=0 line.
    for i in flights:
        if i[0] == src:
            dp[0][i[1]] = i[2]
    # move one step forward and fill in the dp array, just keep the min value.
    # main slow reason here: 这里dp[k]代表经过了k个中转站到达n城市的最小花费
    # 而第二个解法的dp[k]代表经过至多k个中转站到达n城市的最小花费，所以min函数里面要加上dp[k-1][d]
    # 注意用python更加优雅的写法
    for i in range(1, k+1):
        for j in range(n):
            if dp[i-1][j] != float("inf"):
                for f in flights:
                    if f[0] == j:
                        dp[i][f[1]] = min(dp[i][f[1]], dp[i-1][j]+f[2])
    min_value = dp[0][dst]
    for j in range(1, k+1):
        if dp[j][dst] < min_value:
            min_value = dp[j][dst]
    if min_value != float("inf"):
        return min_value
    else:
        return -1
        
# 164ms why?
def findCheapestPrice(self, n, flights, src, dst, K):
    dp = [[float('inf')]*n for _ in range(K+1)]
    for s, d, v in flights:
        if s == src:
            dp[0][d] = v
    for k in range(1, K+1):
        for s, d, v in flights:                   
            dp[k][d] = min(dp[k-1][d], dp[k-1][s]+v, dp[k][d])
    return dp[K][dst] if dp[K][dst] != float('inf') else -1 

# 改良后的写法，196ms
def cheapest_plane(n, flights, src, dst, K):
    dp = [[float("inf")] * n for _ in range(K+1)]
    # initial K=0 line.
    for i in flights:
        if i[0] == src:
            dp[0][i[1]] = i[2]
    # move one step forward and fill in the dp array, just keep the min value.
    for i in range(1, K+1):
        for s, d, v in flights:
            dp[i][d] = min(dp[i][d], dp[i-1][d], dp[i-1][s]+v)
    return dp[K][dst] if dp[K][dst] != float("inf") else -1     
    
    
if __name__ == "__main__":
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    n = 3
    src = 0
    dst = 2
    k = 1
    print(cheapest_plane(n, flights, src, dst, k))