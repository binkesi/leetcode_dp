# '.' match any single character, '*' match 0 or more last character.
def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    def matches(i, j):
        if i == 0:
            return False
        if p[j-1] == '.':
            return True
        return s[i-1] == p[j-1]
    dp = [[False] * (n+1) for _ in range(m+1)]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] |= dp[i][j - 2]
                if matches(i, j - 1):
                    dp[i][j] |= dp[i - 1][j]
            else:
                if matches(i, j):
                    dp[i][j] |= dp[i - 1][j - 1]
    return dp[m][n]

if __name__ == "__main__":
    s = "bbbba"
    p = ".*a*a"
    print(isMatch(s, p))