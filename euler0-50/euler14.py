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

        def Collatz(n: int, cache={}):
            if n in cache:
                return cache[n]
            if n == 1:
                return 1
            if n % 2 == 0:
                cache[n // 2] = Collatz(n // 2, cache) + 1
                return cache[n // 2]
            else:
                cache[3 * n + 1] = Collatz(3 * n + 1, cache) + 1
                return cache[3 * n + 1]

        max_chain_len, ans = 0, 0
        cache = {}
        for n in range(1, N):
            chain_len = Collatz(n, cache)
            if chain_len > max_chain_len:
                max_chain_len, ans = chain_len, n
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
