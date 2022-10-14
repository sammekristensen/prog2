#!/usr/bin/env python3

from tkinter import N
from person import Person
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))

def main():
	n=11
	f = Person(n)
	print(f.get())
	#f.set(9)
	#print(f.get())

	start=pc()
	print(f"fib of {n} is: {f.fib()}")
	end=pc()
	print(f"k{round(end-start,2)}")
	print(fib_py(n))

if __name__ == '__main__':
	main()
