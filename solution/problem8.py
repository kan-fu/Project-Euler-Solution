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

    def solve(self, K=13):
        """
        Sliding window problem. Keep the window length to K and update the window product by multiplying arr[right]
        and getting divided by arr[left]. Tricky part is that there is 0 in the seq, which will cause trouble
        when moving the left pointer. Modifying 0 to -1 makes the product unable to become the maximum
        while avoiding the divided-by-zero problem. In addition, keep track of the zero count in case two zeros appear
        in the same window.
        """
        seq = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
        arr = list(map(int, seq))
        ans = 0
        window_product, zero_count, left = 1, 0, 0
        for right in range(len(arr)):
            if arr[right] == 0:
                zero_count += 1
                arr[right] = -1
            window_product *= arr[right]
            if right >= K - 1:
                # when window length is equal to K, contract the window
                if zero_count == 0:
                    # calculate maximum only when there is no 0 count and the window length is K
                    ans = max(ans, window_product)
                if arr[left] == -1:
                    zero_count -= 1
                window_product //= arr[left]
                left += 1

        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
