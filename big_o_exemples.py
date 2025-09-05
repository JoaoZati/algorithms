# secção do big O
from utils import run_timeit
import itertools


def func_constant(values: list) -> None:
    print(values[0])


def func_linear(values: list) -> None:
    for val in values:
        print(val)


def func_quadratic(values: list) -> None:
    for value in values:
        for value_2 in values:
            print(value, value_2)


def exemple_o_two_n(values: list) -> None:
    for val in values: print(val)

    for val in values: print(val)


def matcher(lst: list, match: int) -> None:
    for item in lst:
        if item == match:
            return True

    return False


def create_list(n: int) -> list:
    """
    O(n) in complexity and memory
    """
    return list(range(n))


def printer(n: int) -> None:
    """
    O(n) only in complexity not in memory
    """

    for x in range(n):
        print("hello word")


def power_set(nums):
    """
    Exemple O(2^n)
    """
    subsets = [[]]
    for num in nums:
        # for each existing subset, add the current number
        subsets += [s + [num] for s in subsets]
    return subsets



def generate_permutations(arr):
    """
    Exemple 2! (calculate permutation)
    """

    return list(itertools.permutations(arr))


if __name__ == '__main__':
    values: list = [1, 2, 3, 4, 5, 6]

    run_timeit(func_constant, values, number=1)
    run_timeit(func_linear, values, number=1)
    run_timeit(func_quadratic, values, number=1)
    run_timeit(exemple_o_two_n, values, number=1)
    # O(1)
    run_timeit(matcher, values, 1, number=1)
    # O(n)
    run_timeit(matcher, values, 11, number=1)

    # O(2^n)
    run_timeit(power_set, [1, 2, 3], number=1)

    # O(n!)
    run_timeit(generate_permutations, [1, 2, 3], number=1)
