#!/usr/bin/env python3

from tkinter import N
from person import Person
from time import perf_counter as pc
from numba import njit

def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))


def main():
	n=30
	f = Person(n)
	print(f.get())
	#f.set(9)
	#print(f.get())

	start1=pc()
	print(f"fib of {n} is, calculated in c++: {f.fib()}")
	end1=pc()
	print(f"time for c++: {round(end1-start1,2)}")

	start2=pc()
	print(f"fib of {n} is:{fib_py(n)}")
	end2=pc()
	print(f"time for fib_py, calculated in py: {round(end2-start2,2)}")

	@njit
	def fib_numba(n):
		if n <= 1:
			return n
		else:
			return (fib_py(n-1) + fib_py(n-2))

	print(f"fib of {n} is:{fib_numba(n)}")
	
if __name__ == '__main__':
	main()
