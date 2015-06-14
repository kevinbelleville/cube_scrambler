import time

def timer():
	input("Press 'Enter' to start timer.")
	start = time.time()
	input("Press 'Enter' to end timer.")
	end = time.time()
	_time = "{0:.2f}".format(end-start)
	print(_time)
	return _time

if __name__ == "__main__":
	timer()