import time
import logging

logging.basicConfig(level=logging.INFO)


def log_time(func):
    def wrapper(*args, **kwargs):
        s_time = time.time()
        res = func(*args, **kwargs)
        e_time = time.time()
        exec_time = e_time - s_time
        logging.info(f"Executed {func.__name__} in {exec_time:.4f} seconds")
        return res

    return wrapper


@log_time
def fibonacci(n):
    def fib_recursion(n):
        if n == 1 or n == 2:
            return 1
        return fib_recursion(n - 1) + fib_recursion(n - 2)
    return fib_recursion(n)


if __name__ == "__main__":
    n = 35
    res = fibonacci(n)
    print(f"Fibonacci value of {n}: {res}")
