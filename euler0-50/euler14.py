class Solution:
    def __init__(self):
        import time

        start = time.time()
        self.answer = self.solve()
        elapse = time.time() - start
        if elapse > 1:
            self.time = f"{elapse:.1f}s"
        else:
            self.time = f"{elapse*1000:.1f}ms"

    def solve(self, N=1000000):
        """
        DFS with memoization
        """

        def Collatz(n: int, cache: dict[int, int] = {}) -> int:
            if n in cache:
                return cache[n]
            if n == 1:
                return 1
            if n % 2 == 0:
                cache[n] = Collatz(n // 2, cache) + 1
                return cache[n]
            else:
                cache[n] = Collatz(3 * n + 1, cache) + 1
                return cache[n]

        max_chain_len, ans = 0, 0
        cache = {}
        for n in range(1, N):
            chain_len = Collatz(n, cache)
            if chain_len >= max_chain_len:
                max_chain_len, ans = chain_len, n
        return ans

    def solve2(self, N=1000000):
        """
        Version for hackerrank. Key modifications are:
        1. cache is converted to list since key are all integers to avoid dictionary overhead. But for N=5*10**6,
        the upper bound can be extremely large (1318802294932), and it is highly unlikely that this number will be reused
        often. So cache has a CACHE_MAX upper bound and Collatz only cache n that is less than CACHE_MAX
        2. Since we need to calculate up to 10^4 in one run, we only need to precompute for the maximum
        N and store the answer in a list.
        """

        def Collatz(n: int, cache: list[int]) -> int:
            if n < CACHE_MAX and cache[n] != 0:
                return cache[n]
            if n == 1:
                return 1
            if n % 2 == 0:
                res = Collatz(n // 2, cache) + 1
            else:
                res = Collatz(3 * n + 1, cache) + 1
            if n < CACHE_MAX:
                cache[n] = res
            return res

        max_chain_len = 0
        CACHE_MAX = 10000000
        cache = [0] * CACHE_MAX
        ans = [0] * (N + 1)

        for n in range(1, N + 1):
            chain_len = Collatz(n, cache)
            if chain_len >= max_chain_len:
                max_chain_len = chain_len
                ans[n] = n
            else:
                ans[n] = ans[n - 1]
        # return ans
        return ans[N]

    # t = int(input().strip())
    # args = []
    # for _ in range(t):
    #     n = int(input().strip())
    #     args.append(n)
    # N = max(args)
    # ans = solve2(N)
    # for n in args:
    #     print(ans[n])


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
