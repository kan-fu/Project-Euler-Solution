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

    def solve2(self, y1=1901, m1=1, d1=1, y2=2000, m2=12, d2=31):
        """
        Check Zeller's Congruence (https://en.wikipedia.org/wiki/Zeller%27s_congruence)
        """

        def zeller(y: int, m: int, d: int):
            """
            formula arguments:
                q: the day of the month
                m: the month (3 = March, 4 = April, 5 = May, ..., 14 = February)
                K: the year of the century (year % 100}).
                J: is the zero-based century (actually year // 100)
                In this algorithm January and February are counted as months 13 and 14 of the *previous* year.
            Returns:
                h: the day of the week (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday)
            """
            q = d
            if m < 3:
                m += 12
                y -= 1
            K = y % 100
            J = y // 100
            h = (q + 13 * (m + 1) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
            return h

        ans = 0
        for year in range(y1, y2 + 1):
            for month in range(1, 13):
                if (
                    year == y1
                    and (month, 1) < (m1, d1)
                    or year == y2
                    and (month, 1) > (m2, d2)
                ):
                    # Exclude days outside of y1-m1-d1 ~ y2-m2-d2
                    continue
                if zeller(year, month, 1) == 1:
                    # 1 = Sunday
                    ans += 1
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
