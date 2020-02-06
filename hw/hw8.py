#We know there will be two possible inputs:
#a string with an odd number of letters or
#a string with an even number of letters
#In each case, we must use a different substring
#in order to get the desired results
#For example, 'attta', we need to compare the middle letter
#So the first substring would be 'att' and the second 'tta'
#We then reverse the second string and compare it the first
#if they match, then that is a palindrome
#In the second case, with an even number of letters,
#we can split the string in half, we an even number of letters
#on each half, first and second
#For example, 'atta' would be split into 'at' and 'ta'
#We then reverse the second and compare it to the first
#In this case we would find they match, and the function returns True

def palindrome(myStr):
	if len(myStr)%2 == 0: # if the string has an even number
		first = myStr[0:len(myStr)//2]
		second = myStr[len(myStr)//2:]
		second = second[::-1]
		if first == second:
			return True
		return False

	first = myStr[0:(len(myStr)//2) + 1]
	second = myStr[(len(myStr)//2):]
	second = second[::-1]
	print(first)
	print(second)
	if first == second:
		return True
	return False



def test(myStr):
	if myStr == myStr[::-1]:
		return True
	return False




#know that if there are fewer than 1 steps
#then the number of solutions would be zero
#If there is a single step, then there is a single solution
#If there are two steps, then there are two solutions, 1+1 and 2
#If there are three steps, there are four solutions,
#1+1+1 or 1+2 or 2+1 or 3
#Since we only ever subtract by three, 
#we do not need to establish any more constants
#Go through and subtract out one until 
#the end to get the number of steps there
#Then subtract 2 and go through that recursion 
#until you get to the number of steps that way
#Then subract 3 and go throuh that recursion 
#until you get to the number of steps that way
#Collapes recursion 
#and add up all of the totals found through the recursion
#Return the totals

def countStairs(numStairs):
	if numStairs < 1:
		return 0
	elif numStairs == 1:
		return 1 #1
	elif numStairs == 2:
		return 2 #1+1 or 2
	elif numStairs == 3:
		return 4 #1+1+1 or 1+2 or 2+1 or 3
    # Test Case countStairs(4) = 7  --> 1+1+1+1 1+1+2 1+2+1 2+1+1 2+2 1+3 3+1   TRUE
    
	else:
		print("Got to the else statement")
		return countStairs(numStairs - 1) + countStairs(numStairs - 2) + countStairs(numStairs - 3)


