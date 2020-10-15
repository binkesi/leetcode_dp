def drop_egg(K, N):
    memo = {}
    def dp(k, n):
        if (k, n) not in memo:
            if n == 0:
                ans = 0
            elif k == 1:
                ans = n
            else:
                lo, hi = 1, n
                while lo + 1 < hi:
                    x = (lo + hi) // 2
                    t1 = dp(k-1, x-1)
                    t2 = dp(k, n-x)
                    if t1 < t2:
                        lo = x
                    elif t1 > t2:
                        hi = x
                    else:
                        lo = hi = x
                ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x)) for x in (lo, hi))
            memo[(k, n)] = ans
        return memo[(k, n)] 
    return dp(K, N)
    
def drop_egg_dp(K, N):
    dp = list(range(N+1))
    dp2 = [0] * (N+1)
    for k in range(2, K+1):
        x = 1
        for n in range(1, N+1):
            while x < n and max(dp[x-1], dp2[n-x]) >= max(dp[x], dp2[n-x-1]):
                x += 1
            dp2[n] = 1 + max(dp[x-1], dp2[n-x])
        dp = dp2[:]
        print(dp, dp2)
    return dp[-1]
    
# math method
def drop_egg_math(K, N):
    if N == 1:
        return 1
    dp = [[0] * (K+1) for _ in range(N+1)]
    for k in range(1, K+1):
        dp[1][k] = 1
    ans = -1
    for t in range(2, N+1):
        for k in range(1, K+1):
            dp[t][k] = 1 + dp[t-1][k-1] + dp[t-1][k]
        if dp[t][-1] >= N:
            ans = t
            break
    return ans

if __name__ == "__main__":
    N = 10
    K = 3
    print(drop_egg(K, N))
    print(drop_egg_dp(K, N))
    print(drop_egg_math(K, N))
    