from random import choice
import time

length = 25
faces = ['R','U','F','D','B','L']
types = ["","'","2"]
moves = {}
for face in faces:
	moves[face] = types
log = {}
times =[]

def opposite_face(orig):
	if orig == 0:
		return "poop"
	opposites = ["L", "D", "B", "U", "F", "R"]
	return opposites[faces.index(orig)]

def timer():
	input("Press 'Enter' to start timer.")
	start = time.time()
	input("Press 'Enter' to end timer.")
	end = time.time()
	_time = "{0:.2f}".format(end-start)
	print(_time)
	times.append(_time)
	return _time

def scramble():
	scram = ""
	face_choice = [0]
	for i in range(length):
		face = choice(faces)
		while face == face_choice[i] or face == opposite_face(face_choice[i]):
			face = choice(faces)
		face_choice.append(face)
		scram += face+choice(types)+" "
	print(scram)
	log[scram] = timer()

def average():
	avg = 0
	if len(times) >= 5:
		for i in range(len(times)):
			avg += float(times[i])
	avg = avg/len(times)
	print("Your average is:", str(avg))

def view_log():
	ans = input("Do you want to see the log?")
	if ans.lower() == "yes":
		for key in log:
			print(log[key],"|", key)

def main():
	while True:
		scramble()
		again = input("Do you want to solve another scramble?")
		if again.lower() == "no":
			view_log()
			average()
			print("Thanks for using Cube Scrambler 1.0 by Kevin Belleville!")
			return
		elif again.lower() == "yes":
			print("Okay, here's another scramble comin' at ya!")
		else:
			print("Invalid input!")
			break


if __name__ == "__main__":
	main()
