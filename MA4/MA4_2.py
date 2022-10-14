#!/usr/bin/env python3

from tkinter import N
from person import Person
from time import perf_counter as pc
from numba import njit
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return (fib_numba(n-1) + fib_numba(n-2))



def main():

	n = list(range(20,30+1))
	fib_py_lst=[]
	fib_numba_lst=[]
	fib_cpp_lst=[]

	for n in range(20,30):

		f = Person(n)

		start1=pc()
		f.fib()
		end1=pc()
		time1=round(end1-start1,2)
		fib_cpp_lst.append(time1)

		start2=pc()
		fib_py(n)
		end2=pc()
		time2=round(end2-start2,2)
		fib_py_lst.append(time2)
		
		start3=pc()
		fib_numba(n)
		end3=pc()
		time3=round(end3-start3,2)
		fib_numba_lst.append(time3)
	
	fig, axs = plt.subplots(3, sharex=True, sharey=True)
	axs[0].bar(n,fib_py_lst)
	axs[1].bar(n,fib_numba_lst)
	axs[2].bar(n,fib_cpp_lst)
	fig.savefig("the_barchart.jpeg")

	

if __name__ == '__main__':
	main()
