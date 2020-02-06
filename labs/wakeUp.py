#This line is a comment) using integers to represent time as minutes
def wakeUpM (leave, duration):
	return leave - duration



def wakeUpNaive(leave, duration):
	return (leave[0] - duration[0], leave[1] - duration[1])
# This misses the fact that there are 60 minutes in an hour



def wakeUp (l, d):
	if (l[1] < d[1]):
		return (l[0] - d[0] - 1, 60 + l[1] - d[1])
	else:
		return (l[0] - d[0], l[1] - d[1])



def timeToMinutes (time):
	return time[0]*60 + time[1]



def minutesToTime(minutes):
	return (minutes // 60, minutes % 60)


def wakeUpF(wakeUpTime, getReadyTime):
	if(wakeUpTime[1] < getReadyTime[i]):
		return

