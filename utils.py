import timeit


def run_timeit(func: callable, *args, number=1_000, **kwargs) -> timeit.timeit:
    wrapped = lambda: func(*args, **kwargs)
    t = timeit.timeit(wrapped, number=number)
    print(f"{func.__name__}({args}, {kwargs}) ran {number}x in {t:.6f} seconds")
    return t
