import math
'''def f(num):
	r = num/2
	while abs(num - (r**2)) > 0.00000000000001 :
		r = (r+(num/r))/2
	return r


def f(letter):
	if (letter < "A") or (letter > "Z"):
		return False
	else:
		return True'''

def f(n):
	for i in range(n):
		for j in range(n):
			res = i*j
			print(str(res), end=" ")
		print()
