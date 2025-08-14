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
        """
        Classic dynamic programming problem. Let dp[i][j] be the maximum total starting from
        triangle[i][j], we want to find dp[0][0]. The state transition equation is
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j], meaning for position (i, j), we will
        choose the larger adjacent number in the next level. Dynamic programming problem can usually
        be solved through bottom-up (tabulation) or top-down (memoization) approach.
        """
        triangle = [
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
        ]
        m = len(triangle)

        def dp(i, j, cache={}):
            if i == m - 1:
                return triangle[i][j]
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = (
                max(dp(i + 1, j, cache), dp(i + 1, j + 1, cache)) + triangle[i][j]
            )
            return cache[(i, j)]

        return dp(0, 0)

    def solve2(self):
        """
        In bottom-up (tabulation) approach, we start from the bottom level, and go up level by level
        """
        triangle = [
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
        ]
        m = len(triangle)
        # add one more layer in dp to skip the initialization. Otherwise we need to initialize
        # the last level first: d[m-1][j] = triange[m-1][j] for j in range(m), meaning when there
        # is only one level, the maximum sum is the matrix value itself
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in reversed(range(m)):
            for j in range(i + 1):
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
