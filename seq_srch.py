#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  seq_srch.py
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

def next_f(F):
	F[0]=F[1]
	F[1]=F[2]
	F[2]=F[0]+F[1]
	return F

def main(args):
	F = ['a','b','ab']
	stride = 21
	while len(F[2]) < stride*6:
		F = next_f(F)
	print(F[2])
	print()
	
	w = 3
	e = stride
	while e < len(F[2]):
		a = F[2][w:e]
		print(a,len(a))
		w = e
		e = e+stride

	
	
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
