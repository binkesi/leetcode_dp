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
        

if __name__ == "__main__":
    n = 21
    k = 17
    w = 10
    print(new_21(n, k, w))