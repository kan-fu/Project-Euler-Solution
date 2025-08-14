def solve(n=1000):
    return sum(i for i in range(0, n) if i % 3 == 0 or i % 5 == 0)


def solve2(n=1000):
    def arithmetic_sum(x, p):
        return p * (x // p) * (x // p + 1) // 2

    return (
        arithmetic_sum(n - 1, 3) + arithmetic_sum(n - 1, 5) - arithmetic_sum(n - 1, 15)
    )


if __name__ == "__main__":
    print(solve())
