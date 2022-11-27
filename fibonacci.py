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

class Fibonacci:
	
	fd = {}
	
	def __init__(self):
		self.fa = (0,0)	#(idx,value)
		self.fb = (1,1)
		self.fc = (2,1)
	
	def get_fib(self,idx = None):
		if idx == None:
			return self.fc
		else:
			while self.fc[0] < idx:
				self.fa = self.fb
				self.fb = self.fc
				self.fc = (self.fc[0] + 1, self.fa[1] + self.fb[1])
			return (self.fc)




def main(args):
	fn = Fibonacci()
	print(fn.get_fib())
	print(fn.get_fib(5))
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
