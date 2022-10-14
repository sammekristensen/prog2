#!/usr/bin/env python3

from person import Person

def main():
	n=5
	f = Person(n)
	print(f.get())
	f.set(9)
	print(f.get())
	print(f"fib of {n} is: {f.fib()}")

if __name__ == '__main__':
	main()
