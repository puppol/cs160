#This is a comment

weeks = 6
def days(w):
	return w*7


def minutes(days):
	return days*1440


minInYear = minutes(days(52))
print(str(minInYear))

def squares(a,b):
	a2 = a**2
	b2 = b**2
	ab = a2+b2
	return ab


