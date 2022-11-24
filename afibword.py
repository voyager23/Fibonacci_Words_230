#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  afibword.py
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
'''
	Notes:
	z = [((127 + 19*n)*7**n) for n in range(18)]
	[127, 1022, 8085, 63112, 487403, 3731154, 28353409, 214121180, 1608379479, 12025374886, 89544653933, 
	664381785648, 4913656956355, 36236489892218, 266541667629657, 1955995342096516, 14323393075498031, 104683731294243150]
	A = '1415926535'
	B = '8979323846'
	Fab = [A,B,A+B]
	The length of the 5th term in F is (Fibonacci(5) * len(A)) = 5 * 10 = 50
	The length of the 4th term in F is (Fibonacci(4) * len(A)) = 3 * 10 = 30
	Fibonacci(7) = 13 so 7th term has 130 characters
	
	Construct a random ascending sequence of 17 integers 1 <= i <= 130
	11,23,29,37,41,51,57,83,87,91,99,101,111,119,123,129,130
	Fab[6] is 7th term
	 
'''

def FAB(t):
	Fab = ['A','B']
	if t < 3:
		return Fab
	while t > 2:
		Fab.append(Fab[-2]+Fab[-1])
		t -= 1
	return Fab
	

def main(args):
	A = '1415926535'
	B = '8979323846'
	F = FAB(7)
	t = 29
	for i in range(len(F)):
		if len(F[i]*10) >= t:
			break
	print(i, F[i])
	#A,B selector
	if F[i][t//10] == 'A':
		print(A[t%10 - 1])
	else:
		print(B[t%10 - 1])
		

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
