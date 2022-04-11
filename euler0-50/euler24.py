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

    def solve(self, seq=1000000, digits="0123456789"):
        """
        | seq | perm  | seq // 2! | seq % 2! |
        |-----|-------|-----------|----------|
        | 0   | 0 1 2 |     0     |     0    |
        | 1   | 0 2 1 |     0     |     1    |
        | 2   | 1 0 2 |     1     |     0    |
        | 3   | 1 2 0 |     1     |     1    |
        | 4   | 2 0 1 |     2     |     0    |
        | 5   | 2 1 0 |     2     |     1    |

        Consider N=3 digits permutations of 012, in total there are N!=6 permutations.
        Fix the most significant digit, we see there are (N-1)!=2 permutations. In other words,
        for the pattern going from 0XX to 1XX, there are (N-1)! steps to make, so the
        perm[0] = seq // (N-1)!. If we look at seq=3, seq // 2! = 1, so the problem reduces to
        find the NO. seq % 2! = 1 perm from digits 02 (excluding the chosen digit),
        which is 20. So the seq = 3 perm of 012 is 120.
        The whole process is like converting the decimal number N into a new number
        where the base is not 10^0, 10^1, ..., 10^n, but 1!, 2!, ..., n!.
        """
        import math

        N = len(digits) - 1
        ans = []
        seq -= 1  # modify to 0-indexed sequence
        for n in reversed(range(N + 1)):
            base = math.factorial(n)
            i = seq // base
            ans.append(digits[i])
            digits = (
                digits[:i] + digits[i + 1 :]
            )  # Exclude the selected digit from candidates
            seq %= base

        return "".join(ans)


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
