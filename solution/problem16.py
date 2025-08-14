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

    def solve(self, N=1000):  
        return sum(map(int, str(2**N)))

    def solve2(self, N=1000):
        n, s = 2**N, 0
        while n:
            s += n % 10
            n //= 10
        return s


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
