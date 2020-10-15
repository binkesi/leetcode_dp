def countsub(S):
    n = len(S)
    mod = 1000000007
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            for k in range(4):
                c = chr(ord('a') + k)
                if i == j:
                    if S[i] == c:
                        dp[k][i][j] = 1
                    else:
                        dp[k][i][j] = 0
                else:
                    if S[i] != c:
                        dp[k][i][j] = dp[k][i+1][j]
                    elif S[j] != c:
                        dp[k][i][j] = dp[k][i][j-1]
                    else:
                        if j == i+1:
                            dp[k][i][j] = 2
                        else:
                            dp[k][i][j] = 2
                            for x in range(4):
                                dp[k][i][j] += dp[x][i+1][j-1]
                                dp[k][i][j] %= mod
    print(dp)
    ans = 0
    for k in range(4):
        ans += dp[k][0][n-1]
        ans %= mod
    return ans        


if __name__ == "__main__":
    s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
    # ans = 104860361
    print(countsub(s))