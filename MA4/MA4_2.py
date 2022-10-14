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

#	nn = list(range(30,45+1))
#	fib_py_lst=[]
#	fib_numba_lst=[]
#	fib_cpp_lst=[]


#	for n in range(30,45+1):
#
#		f = Person(n)
#
#		start1=pc()
#		f.fib()
#		end1=pc()
#		time1=round(end1-start1,2)
#		fib_cpp_lst.append(time1)
#
#		start2=pc()
#		fib_py(n)
#		end2=pc()
#		time2=round(end2-start2,2)
#		fib_py_lst.append(time2)
#		
#		start3=pc()
#		fib_numba(n)
#		end3=pc()
#		time3=round(end3-start3,2)
#		fib_numba_lst.append(time3)
#
#		print(f"done with fib({n})")

#	nnn=list(range(20,30+1))
#	fib_py_lst2=[]
#	fib_numba_lst2=[]

#	for n2 in range(20,30+1):

#		start2=pc()
#		fib_py(n2)
#		end2=pc()
#		time2=round(end2-start2,2)
#		fib_py_lst2.append(time2)
#		
#		start3=pc()
#		fib_numba(n2)
#		end3=pc()
#		time3=round(end3-start3,2)
#		fib_numba_lst2.append(time3)
#
#		print(f"done with fib({n2})")


	#fig1, axs = plt.subplots(2,2)
	#axs[0,0].stem(nn,fib_py_lst,linefmt='--')
	#axs[0,0].set_title('fib_py')
	#axs[0,1].stem(nn,fib_numba_lst,linefmt='--')
	#axs[0,1].set_title('fib_numba')
	#axs[1,0].stem(nn,fib_cpp_lst,linefmt='--')
	#axs[1,0].set_title('fib_cpp')
	#fig1.savefig("the_barchart.jpeg")
#
#	fig2, axs = plt.subplots(2)
#	axs[0].stem(nnn,fib_py_lst2,linefmt='--')
#	axs[0].set_title('fib_py')
#	axs[1].stem(nnn,fib_numba_lst2,linefmt='--')
#	axs[1].set_title('fib_numba')
#	fig2.savefig("thing2.jpeg")

	f = Person(47)
	fib_cpp_ = f.fib()
	fib_numba_ = fib_numba(47)
	print(f"fib(47) using c++: {fib_cpp_}")
	print(f"fib(47) using numba: {fib_numba_}")

if __name__ == '__main__':
	main()
