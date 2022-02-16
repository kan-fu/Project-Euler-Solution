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

    def solve(self, N=100):
        sum_square = N * (N + 1) * (2 * N + 1) // 6
        square_sum = N * N * (N + 1) * (N + 1) // 4
        return square_sum - sum_square


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
