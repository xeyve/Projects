#!/bin/python3
import sys
a = 0
b = 1
c = 1
i = 0
e = int(sys.argv[1]) - 1
print(a, end="")
print(", ", end="")
while i < e :
	print(str(b), end="")
	print(", ", end="")
	c = a
	a = b
	b = b + c 
	i = i + 1

print("\b\b" +" ")
