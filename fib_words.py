#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  fib_words.py
#  
#  Copyright 2022 Mike <mike@pop-os>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  



def main(args):
	
	A='1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
	 
	B='8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'
	
	F = [('A',100),('B',100),('AB',200)]
	
	Sum = 0
	
	for n in range(18):
		p = ((127 + 19*n)*7**n)
		while F[2][1] < p:
			F[0] = F[1]
			F[1] = F[2]
			F[2] = (F[0][0]+F[1][0], F[0][1]+F[1][1])
		# extract the pth digit from F[2]
		if F[2][0][(p-1)//100] == 'A':
			Sum += int(A[(p-1)%100]) * 10**n
		else:
			Sum += int(B[(p-1)%100]) * 10**n
		print(f"n:{n}	Sum:{Sum}")
		
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
