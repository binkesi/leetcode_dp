def new_21(n, k, w):
    dp = [0] * w
    dp[-1] = (n-k+1)/w
    for i in range(w-2, -1, -1):
        dp[i] = (1/w * dp[i+1]) + (dp[i+1]-)
        

if __name__ == "__main__":
    n = 21
    k = 17
    w = 10