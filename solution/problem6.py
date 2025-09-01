def solve(n=100):
    sum_square = n * (n + 1) * (2 * n + 1) // 6
    square_sum = n * n * (n + 1) * (n + 1) // 4
    return square_sum - sum_square


if __name__ == "__main__":
    print(solve())
