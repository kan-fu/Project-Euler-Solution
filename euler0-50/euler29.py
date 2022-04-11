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

        return len({a**b for a in range(2, N + 1) for b in range(2, N + 1)})

    def solve2(self, N=100000):
        """
        All credits go to WP (https://projecteuler.net/thread=29;page=5). The code below is
        a mere translation from WP's java code. Basic idea is to count duplicates when a is a
        nth power. For example, if a is 81 = 3^4, then part of powers of 81 must be duplicate
        with those of 27 (3^3), 9(3^2) and 3 (3^1).
        """
        import math

        max_power, prod = 0, 1
        while prod <= N:
            prod *= 2
            max_power += 1
        dupes_power = [0] * max_power
        num_of_power = [0] * max_power
        total_dupes = 0

        for i in range(2, max_power):
            power_overlap = [False] * (N + 1)
            for k in range(1, i):
                spacing = math.lcm(k, i) // i
                for n in range(0, k * N // i + 1, spacing):
                    power_overlap[n] = True
            dupes_power[i] = sum(power_overlap[2:])

        sqrtN = int(math.sqrt(N))
        powers_not_repeat = [False] * (sqrtN + 1)
        for i in range(2, sqrtN + 1):
            if not powers_not_repeat[i]:
                p, power = 2, i**2
                while power <= N:
                    num_of_power[p] += 1
                    if power <= sqrtN:
                        powers_not_repeat[power] = True
                    p += 1
                    power *= i

        for p in range(2, max_power):
            total_dupes += num_of_power[p] * dupes_power[p]
        return (N - 1) ** 2 - total_dupes


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
