def new_21(n, k, w):
    if k == 0:
        return 1
    dp = [0] * (k+w)
    for i in range(k, min(n, k+w-1)+1):
        dp[i] = 1
    for i in range(k-1, -1, -1):
        for j in range(1, w+1):
            dp[i] += dp[i+j]/w
    return dp[0]
    
def new_21_dp(N, K, W):
    if K == 0:
        return 1
    dp = [0] * (K+W)
    for i in range(K, min(N, K+W-1)+1):
        dp[i] = 1
    dp[K-1] = float(min(N-K+1, W)/W)
    for i in range(K-2, -1, -1):
        dp[i] = dp[i+1] - (dp[i+W+1] - dp[i+1])/W
    return dp[0]
        

if __name__ == "__main__":
    n = 21
    k = 17
    w = 10
    print(new_21(n, k, w))
    print(new_21_dp(n, k, w))