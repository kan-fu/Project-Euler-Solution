def solve(n=20):
    from math import gcd

    ans = 1
    for i in range(2, n + 1):
        ans *= i // gcd(ans, i)
    return ans


def solve2(n=20):
    from math import lcm

    return lcm(*[i for i in range(1, n + 1)])


if __name__ == "__main__":
    print(solve())
