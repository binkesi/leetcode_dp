def maxDotProduct(nums1, nums2) -> int:
    m, n = len(nums1), len(nums2)
    dp = [[-float("inf")] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = nums2[i-1]*nums1[j-1]
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            dp[i][j] = max(dp[i][j], dp[i][j-1])
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + nums2[i-1]*nums1[j-1])
    return dp[n][m]
        

if __name__ == "__main__":
    nums1 = [-3,-8,3,-10,1,3,9]
    nums2 = [9,2,3,7,-9,1,-8,5,-1,-1]
    print(maxDotProduct(nums1, nums2))