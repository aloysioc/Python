from datetime import timedelta
def add_gigasecond(datag):

	seg = datag + timedelta(seconds=10**9)
	return seg
	
