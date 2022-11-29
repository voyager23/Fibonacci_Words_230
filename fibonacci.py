#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  fibonacci.py
#  
#  Copyright 2022 Mike <mike@pop-os>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class Fibonacci():

	def __init__(self):
		self.fn = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
			1597,2584,4181,6765,10946,17711,28657,46368,75025,
			121393,196418,317811,514229,832040,1346269,
			2178309,3524578,5702887,9227465,14930352,24157817,
			39088169,63245986,102334155]
		# compute the dictionary from data
		self.fd = {}
		for i in range(len(self.fn)):
			self.fd[i] = self.fn[i]
	
	def get_fib(self,idx = None):
		if idx == None:
			return self.fd[0]
		else:
			# if idx in dict return value
			try:
				return self.fd[idx]
			# else xtend dict and return last value
			except KeyError:
				# get hi-idx
				hi_idx = sorted(self.fd)[-1]
				# extend dictionary
				while hi_idx < idx:
					hi_idx += 1
					self.fd[hi_idx] = self.fd[hi_idx-1] + self.fd[hi_idx-2]
				return self.fd[hi_idx]

def main(args):
	fn = Fibonacci()
	print(fn.get_fib())
	print(fn.get_fib(5))
	print(fn.get_fib(38))
	print(fn.get_fib(39))
	print(fn.get_fib(40))
	print(fn.get_fib(41))
	print(fn.get_fib(38))
	print(fn.get_fib(39))
	print(fn.get_fib(40))
	print(fn.fd)
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
