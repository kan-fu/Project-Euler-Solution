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
        1 ~ 1000 numbers can be categorized into 1 ~ 19, 20 ~ 99, 100 ~ 999, 1000.
        - 1 ~ 19 has their own words;
        - 20 ~ 99 has tens digit + ones digit (e.g., 29 is twenty nine)
        - 100 ~ 999 has two cases. Numbers like 100, 200 is hundred digit + hundred, while others need "and" in between.
            tens digit and ones digit can be retrieved from previous calculation
        - 1000 is one thousand
        """
        ones = [
            "",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ]
        tens = [
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
        ]
        hundred = "hundred"
        one_thousand = "onethousand"
        ans = 0
        cache = {}  # store word length under 100
        for n in range(1, N):
            if n < 20:
                cache[n] = len(ones[n])
                ans += cache[n]
            elif n < 100:
                tens_digit, ones_digit = n // 10, n % 10
                cache[n] = len(tens[tens_digit - 2]) + len(ones[ones_digit])
                ans += cache[n]
            else:
                hundred_digit, tens_ones_digits = n // 100, n % 100
                if tens_ones_digits == 0:
                    ans += len(ones[hundred_digit]) + len(hundred)
                else:
                    ans += (
                        len(ones[hundred_digit])
                        + len(hundred)
                        + len("and")
                        + cache[tens_ones_digits]
                    )
        ans += len(one_thousand)
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
