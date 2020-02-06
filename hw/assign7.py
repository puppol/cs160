def addOne(args):
	addedOneList = []
	for x in range(len(args)):
		addedOneList.append(args[x] + 1)
	return addedOneList

print(addOne(1,2,3))

def rawGradeToLetter(num):
    if num < 60:
        return 'F'
    elif num < 70:
        return 'D'
    elif num < 80:
        return 'C'
    elif num < 90:
        return 'B'
    else:
        return 'A'

def convertRawsToLetters(args):
    gradeLetterList = []
    for x in range(len(args)):
        gradeLetterList.append(rawGradeToLetter(args[x]))
    return gradeLetterList

def ouncesToCups(args):
    cupList = []
    for x in range(len(args)):
        cupList.append(args[x]*0.125)
    return cupList

def glassesOfWater(args):
    return ouncesToCups(*args)

def hydrated(ozConsumed):
    glasses = glassesOfWater(ozConsumed)
    if glasses[0] > 8:
        return "Hydrated"
    else:
        return "Not hydrated"

def waterNeeded(ozConsumed):
    if hydrated(ozConsumed) == "Hydrated":
        return 0
    else:
        glasses = glassesOfWater(ozConsumed)
        return 8 - glasses[0]

