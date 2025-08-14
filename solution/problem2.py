def solve(n=4 * 10**6):
    a, b = 1, 2
    ans = 0
    while b < n:
        if b % 2 == 0:
            ans += b
        b, a = a + b, b
    return ans


if __name__ == "__main__":
    print(solve())
