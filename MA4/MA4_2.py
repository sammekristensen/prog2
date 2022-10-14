#!/usr/bin/env python3

from tkinter import N
from person import Person

def fib_py(n):
    if n ==0:
        return 0
    elif n ==1:
         return 1
    else:
        return fib_py(n-1) + fib_py(n-2)

def main():
	n=5
	f = Person(n)
	print(f.get())
	f.set(9)
	print(f.get())
	print(f"fib of {n} is: {f.fib()}")
	print(fib_py(n))

if __name__ == '__main__':
	main()
