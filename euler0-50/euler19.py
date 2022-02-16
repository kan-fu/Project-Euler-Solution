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

    def solve(self):
        import datetime

        ans = 0
        for year in range(1901, 2001):
            for month in range(1, 13):
                if datetime.date(year, month, 1).weekday() == 6:
                    ans += 1
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
