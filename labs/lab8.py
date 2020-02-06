def containsNum (n, arr):
	for i in range(len(arr)):
		if arr[i] == n:
			print("Success!")

def printLast(arr):
	while len(arr) != 1:
		arr = arr[1:]
	return arr


def printReverse(arr):
	arrRev = [None] * len(arr)
	for i in range(len(arr)):
		arrRev[len(arr) - 1 - i] = arr[i]
	return arrRev
