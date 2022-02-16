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

    def solve(self, N=20):
        from math import gcd

        ans = 1
        for i in range(2, N + 1):
            ans *= i // gcd(ans, i)
        return ans

    def solve2(self, N=20):
        from math import lcm

        return lcm(*[i for i in range(1, N + 1)])


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
