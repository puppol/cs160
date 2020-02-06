
#----------------------------------------------------------------------
#-- REPRESENTATIONS
#----------------------------------------------------------------------


home = (3.0,4.5)

pebbles = [(9,8), (6,8.5), home]

#----------------------------------------------------------------------
#-- OPERATIONS ON POSITIONS
#----------------------------------------------------------------------


def moveRightBy (n, pos):
	return (pos[0]+n, pos[1])

#compute distance function with two coordinate points
def distance (pos1, pos2):
	return (((pos2[0]-pos1[0])**2)+((pos2[1]-pos1[1])**2))**(1/2)

# Finding the smallest element in a list
def smallest (arr):
	min = arr[0]
	for i in range(len(arr)):
		if min > arr[i]:
			min = arr[i]
	return min

# Finding the closest pebble in a list (Not discluding current position)
def closestTo (currentPos, path):
	minDist = 100
	index = -1
	for i in range(len(path)):
		if distance(currentPos, path[i]) < minDist:
			minDist = distance(currentPos, path[i])
			index = i
	return path[i]

#
# ----------------------------------------------------------------------
# -- OPERATIONS FOR FOLLOWING PEBBLES
# ----------------------------------------------------------------------

# Find home alogrithm that looks for the closest pebble and adds it to the path. 
# Doesn't take into account that it will forever be stuck at the same pebble.
def findHome1 (currentPos, path):
	pathTaken = []
	while(currentPos != home):
		currentPos = closestTo(currentPos, path); 
		pathTaken += currentPos;
	return pathTaken

###### New ClosestTo functon that takes into account not styaing at the same pebble ###
def closestToNew (currentPos, path):
	minDist = 0
	minDistLoc = ()
	for i in range(len(path)):
		dist = distance(currentPos, path[i])
		if minDist == 0:
			minDist = dist
			minDistLoc = path[i]
		elif (dist < minDist) and (currentPos != path[i]):
			minDist = dist
			minDistLoc = path[i]
			
	return minDistLoc

# Find home, simlar to first except this time makes sure we move
def findHome2 (currentPos, path):
	pathTaken = []
	while(currentPos != home):
		currentPos = closestToNew(currentPos, path); 
		pathTaken.append(currentPos);
	return pathTaken

###### Helper function for findHome3, it removes places we've been from list possibility
def removeFromList(path, placesVisited):
	for i in range(len(placesVisited)):
		for j in range(len(path)):
			if (path[j] == placesVisited[i]):
				path[j] = (-1, -1)
	return path

#### A new closertTo funciton that also accounts for places we've BEEN ####
def closestToNew2 (currentPos, path, placesVisited):
	minDist = 0
	minDistLoc = ()
	for i in range(len(path)):
		if path[i] not in placesVisited:
			dist = distance(currentPos, path[i])
			if minDist == 0:
				minDist = dist
				minDistLoc = path[i]
			elif dist < minDist:
				minDist = dist
				minDistLoc = path[i]
	return minDistLoc

#Find home three that is the most correct algorithm of the three
#Doesn't go to previously visited pebbles or current pebble
def findHome3 (currentPos, path):
	pathTaken = []
	while(currentPos != home ):
		print(currentPos)
		currentPos = closestToNew2(currentPos, path, pathTaken); 
		pathTaken.append(currentPos);
	return pathTaken
