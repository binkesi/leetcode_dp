def distinctSub(S):
    dp = [1]
    last = {}
    for i, x in enumerate(S):
        dp.append(dp[-1]*2)
        if x in last:
            dp[-1] -= dp[last[x]]
        last[x] = i
    return (dp[-1] - 1)%1000000007


if __name__ == "__main__":
    S = "aba"
    print(distinctSub(S))