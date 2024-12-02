def fib(n: int) -> int:

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    # Example usage
    for i in range(10):
        print(f"fib({i}) = {fib(i)}")
