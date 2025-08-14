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

    def solve(self, N=10000):
        with open("../input/p022_names.txt", "r") as f:
            data = f.read()
        ans = 0
        for i, word in enumerate(sorted(data.split(","))):
            ans += (i + 1) * sum(ord(ch) - ord("A") + 1 for ch in word[1:-1])
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
