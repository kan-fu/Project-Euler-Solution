def solve():
    def isPal(n):
        return str(n) == str(n)[::-1]

    return max(
        i * j for i in range(100, 1000) for j in range(100, 1000) if isPal(i * j)
    )


if __name__ == "__main__":
    print(solve())
