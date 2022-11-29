#!/usr/bin/env python3
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
	
	A=14159265358979323846264338327950288419716939937510\
	58209749445923078164062862089986280348253421170679 
	 
	B=82148086513282306647093844609550582231725359408128\
	48111745028410270193852110555964462294895493038196
	
	#               1046837312942431 (50) in Fib sequence	
		i:73  f73 =  806515533049393
		i:74  f74 = 1304969544928657
'''


import random

#-----------------------------------------------------------------------
def FAB(t):
	Fab = ['A','B']
	if t < 3:
		return Fab
	while t > 2:
		Fab.append(Fab[-2]+Fab[-1])
		t -= 1
	return Fab
	
def z():
	return [((127 + 19*n)*7**n) for n in range(18)] # list of digit positions for main problem

#=======================================================================
fib_dict = { 0:0,1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21,9:34,
10:55,11:89,12:144,13:233,14:377,15:610,16:987,17:1597,18:2584,19:4181,
20:6765,
21:10946,
22:17711,
23:28657,
24:46368,
25:75025,
26:121393,
27:196418,
28:317811,
29:514229,
30:832040,
31:1346269,
32:2178309,
33:3524578,
34:5702887,
35:9227465,
36:14930352,
37:24157817,
38:39088169,
39:63245986,
40:102334155,
41:165580141,
42:267914296,
43:433494437,
44:701408733,
45:1134903170,
46:1836311903,
47:2971215073,
48:4807526976,
49:7778742049,
50:12586269025,
51:20365011074,
52:32951280099,
53:53316291173,
54:86267571272,
55:139583862445,
56:225851433717,
57:365435296162,
58:591286729879,
59:956722026041,
60:1548008755920,
61:2504730781961,
62:4052739537881,
63:6557470319842,
64:10610209857723,
65:17167680177565,
66:27777890035288,
67:44945570212853,
68:72723460248141,
69:117669030460994,
70:190392490709135,
71:308061521170129,
72:498454011879264,
73:806515533049393,
74:1304969544928657,
75:2111485077978050,
76:3416454622906707,
77:5527939700884757,
78:8944394323791464,
79:14472334024676221,
80:23416728348467685,
81:37889062373143906,
82:61305790721611591,
83:99194853094755497,
84:160500643816367088,
85:259695496911122585,
86:420196140727489673,
87:679891637638612258,
88:1100087778366101931,
89:1779979416004714189,
90:2880067194370816120,
91:4660046610375530309,
92:7540113804746346429,
93:12200160415121876738,
94:19740274219868223167,
95:31940434634990099905,
96:51680708854858323072,
97:83621143489848422977,
98:135301852344706746049,
99:218922995834555169026,
100:354224848179261915075}
	

def main(args):
	# Consider a restricted version using 10 digit words 
	# f(12) = 144 => 1440 digits in total
	
	# generate a list of digit positions to sum
	z = sorted([random.randrange(1,1440) for i in range(10)])
	#print(z)
	
	# Method 'A'
	# generate a full list of 1440 digits using 
	A = '1415926535'
	B = '8979323846'
	L = len(A)
	words = 'BAB'
	while len(words) < 144:
		t =''
		for c in words:
			if c == 'A':
				t += 'B'
			else:
				t += 'AB'
		words = t
	# NOTE: words is a zero-based list 0 -> 143
	# print(len(words), words)
	# print(z)
	digits = ''
	for p in z:
		block = (p-1)//L
		posn  = (p-1)%10
		if words[block] == 'A':
			digits += A[posn]
		else:
			digits += B[posn]
	print(digits)
	
	# Method 'B' - assume len(A)==len(B)==10
	# data structure
	# 		ab_word = 'abbab'
	# Clear 'digits'
	# for each digit posn in 'z'
	#		find F(n) >= posn//L
	#		if len(ab_word) < F(n):
	#			extend ab_word until length >= posn
	#		block index = (p-1)//L
	#		if ab_word[block_index] == 'A"
	#			digit = A[(p-1)%10]
	#		else:
	#			digit = B[(p-1)%10]
	#	output digits
	
	ab_word = 'abbab'
	digits = ''
	for p in z:
		i = 0
		while fib_dict[i] < (p//L):	# establish the index
			i += 1
		while len(ab_word) < fib_dict[i]:	# extend the data word if necessary
			temp = ''
			for c in ab_word:
				if c == 'A':
					temp += 'B'
				else:
					temp += 'AB'			
			ab_word = temp
		# find block name and digit
		block_idx = (p-1)//L
		if ab_word[block_idx] == 'A':
			digits += A[(p-1)%10]
		else:
			digits += B[(p-1)%10]
			
	print(digits)
			
		
				
	
	return 0
		

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
