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

    def solve(self, N=1001):
        """
        Consider how to represent the four numbers in a ring. Define the number 1
        as the 0th ring, so 5 by 5 has two rings.
        For example, in the n=2nd ring, the four numbers are 25, 21, 17, 13.
        The largest one is (2n+1)^2, and the four numbers form a arithmetic
        progression with common difference of 2n. So the sum of four numbers
        is (2n+1)^2 + (2n+1)^2-2n + (2n+1)^2-2*2n + (2n+1)^2-3*2n,
        which simplifies to 4*(2n+1)^2 - 6*2n = 16n^2 + 4n + 4. This formula does
        not apply to the 0th ring because it only has one number.
        Sum this term with n from 1 to (1001-1)/2=500 gives us
        16*n*(n+1)*(2n+1)/6 + 4*n*(n+1)/2 + 4n, and the answer is this sum plus
        the 0th ring, which is 1.
        """
        n = (N - 1) // 2
        return 16 * n * (n + 1) * (2 * n + 1) // 6 + 4 * n * (n + 1) // 2 + 4 * n + 1


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
