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
        """
        For n=100, number larger than sqrt(n)=10 can not be 
        """
        
        return len({a**b for a in range(2,N+1) for b in range(2,N+1)})


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
