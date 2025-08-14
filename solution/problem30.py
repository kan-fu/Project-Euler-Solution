

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

    def solve(self, N=5):
        """
        First determine the upper bound of the search space, then brute force.
        Using memoization when calculating the nth power sum would be more time efficient because
        1234567 and 7654321 have the same nth power sum.
        """

        def nth_power_sum(n: int) -> int:
            signature = "".join(sorted(str(n)))
            if signature in cache:
                return cache[signature]
            cache[signature] = sum([int(digit) ** N for digit in signature])
            return cache[signature]

        max_digits = 1
        while 10**max_digits - 1 < 9**N * max_digits:
            max_digits += 1
        max_N = 9**N * max_digits

        ans = 0
        cache = {}
        for n in range(2, max_N):
            if n == nth_power_sum(n):
                ans += n

        return ans

    def solve2(self, N=5):
        """
        In previous solution, we search the number, and might encounter cases
        that have same nth power sum like 7654321 and 1234567.
        We can actually generate a search space that does not include these
        duplicates. For example, if we have 2 spots for digit 0123, we want to only search
        [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
        This is combinations_with_replacement in itertools library. It can be proved that
        the number of combinations with replacement of k objects from n objects is
        math.comb(n+k-1, k), which is way smaller than n**k.

        For each digits in search space, we calculate sorted digits of the nth power sum,
        and compare it with the original digits. Special care is given when actual digits used
        is less than max_digits. For example, when N == 6 and digits == (0, 3, 4, 4, 5, 8, 8),
        max_digits is 7, and the nth power sum is 548834 (only 6 digits), which is essentially
        comprised of (0, 3, 4, 4, 5, 8, 8) but does not have 0.
        """
        # from itertools import combinations_with_replacement

        from collections.abc import Iterable, Iterator

        def combinations_with_replacement(iterable: Iterable, k: int) -> Iterator:
            def backtrack(start):
                if len(comb) == k:
                    yield comb[:]
                else:
                    for i in range(start, len(iterable)):
                        comb.append(iterable[i])
                        yield from backtrack(i)
                        comb.pop()

            comb = []
            return backtrack(0)

        max_digits = 1
        while 10**max_digits - 1 < 9**N * max_digits:
            max_digits += 1

        search_space = combinations_with_replacement(range(10), max_digits)
        ans = 0
        for digits in search_space:
            n = sum([digit**N for digit in digits])
            # remove the leading 0 in the digits
            if n > 1 and int("".join(map(str, digits))) == int("".join(sorted(str(n)))):
                ans += n
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
