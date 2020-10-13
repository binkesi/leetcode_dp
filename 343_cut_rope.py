def cut_rope(n):    
    if n <= 2:
        return 1
    if n == 3:
        return 2
    a = n // 3
    if n % 3 == 1:
        ans = pow(3, a-1) * 4
    elif n % 3 == 2:
        ans = pow(3, a) * 2
    else:
        ans = pow(3, a)
    return ans%1000000007    


if __name__ == "__main__":
    n = 11
    print(cut_rope(n))