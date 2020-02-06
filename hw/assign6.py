def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mult(a,b):
	return a*b

def square(a):
	return a*a

def f1(a,b):
	return sub(add(a,b),5)

def f2(a,b):
	return add(-a,b)

def f3(a):
	return square(-a)

def f4(a,b):
	return add(square(-a),b)

def f5(a):
	first = mult(2,square(a))
	second = mult(3,a)
	return add(add(first,second),5)

def f6(a):
	return square(square(a))

