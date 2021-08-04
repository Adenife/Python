# a program using decorators to check the runtime

from functools import wraps
from math import fsum
from time import perf_counter
from typing import Callable, List, Set

def stopwatch(func: Callable) -> Callable:
	@wraps(func)
	def inner(*args, **kwargs):
		times = []

		for _ in range(10):
			start_time = perf_counter()
			func(*args, **kwargs)
			stop_time = perf_counter()

			elapsed = stop_time - start_time
			times.append(elapsed)

		average_time = fsum(times) / len(times)

		print(f"{func.__name__} ran in {average_time:.5f}s on average")

	return inner

@stopwatch
def make_list(size: int) -> List:
    return list(range(size))

@stopwatch
def make_set(size: int) -> Set:
    return set(range(size))

make_list(100_000)  # make_list ran in 0.00337s on average
make_set(100_000)   # make_set ran in 0.00565s on average