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
        """
        The n-th term of Fibonacci sequence is calculated as
        Fn = 1/sqrt(5) * (phi^n - psi^n)
        where phi = (1+sqrt(5)) / 2 and psi =(1-sqrt(5)) / 2
        Since psi is about -0.618, -psi^n is smaller than 1.
        We want to find the fist n that satisfy
        10^999 <= Fn = 1/sqrt(5) * (phi^n - psi^n) < 1/sqrt(5) * (phi^n - 1)
        Simplify the inequality, we have
        10^999 * sqrt(5) < 10^999 * sqrt(5) + 1 < phi^n
        Log both sides and we can get the lower bound of n
        """
        import math

        phi = (1 + math.sqrt(5)) / 2
        left_hand_log = math.log(math.sqrt(5)) + (N - 1) * math.log(10)
        return int(left_hand_log // math.log(phi)) + 1


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
