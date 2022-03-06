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

    def solve(self, N=20, M=20):
        """
        Think about the 2*2 grid. We need to go 2+2 steps, of which there are 2 steps we need
        to choose to go down (or right). In the example, the first route can be expressed as
        (3,4), meaning at the 3rd and 4th step we choose to go down. The other five routes are
        (2,4), (2,3), (1,4), (1,3) and (1,2). It is exactly the combination formula, choose N
        from 2N.
        """

        from math import comb

        return comb(N + M, N)


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
