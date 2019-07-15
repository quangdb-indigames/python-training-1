import os
import sys
import random

def getUserPoints(userName):
	score = False
	try:
		f = open("userScores.txt", "rt")
		for line in f.readlines():
			list_line = line.split(", ")
			if list_line[0] == userName:
				score = int(list_line[1])
				print(score)
				break
		if not score:
			print("Cant find score of", userName)
	except:
		print("Have some error when get user point!")
	finally:
		f.close()
	return score

def updateUserPoints(userName, points):
	findUser = False
	try:
		f = open("userScores.txt", "rt")
		data = f.readlines()

		for line in data:
			list_line = line.split(", ")
			if list_line[0] == userName:
				index = data.index(line)
				new_line = userName + ", " + str(points) + '\n'
				data.remove(line)
				data.insert(index, new_line)
				findUser = True
				break

		if not findUser:
			new_line = userName + ", " + str(points) + '\n'
			data.append(new_line)
		
		if '\n' in data:
			data.remove('\n')

		f = open("userScores.txt", "w")
		f.writelines(data)
	except:
		print("Have some error when update user point!")
	finally:
		f.close()

def showLeaderBoard():
	try:
		f = open("userScores.txt", "rt")
		data = f.readlines()
		new_data = []
		for line in data:
			list_line = line.split(", ")
			convert = convertFloat(list_line[1])
			if convert == True:
				tuple_data = (list_line[0], float(list_line[1]))
			else:
				tuple_data = (list_line[0], list_line[1])
			new_data.append(tuple_data)

		new_data.sort(key = last_ele, reverse = True)

		for user in new_data:
			print("User: " + user[0] + "	Score: " + str(user[1]))
	except:
		print("Have some error when try to show leader board!!!")
	finally:
		f.close()

def convertFloat(value):
	try:
		float(value)
		return True
	except:
		return False

def last_ele(e):
    return e[-1]

def randomQuestion():
	ops = ["+", "-", "*", "/"]
	# Random number
	rand1 = random.randrange(1, 10)
	rand2 = random.randrange(1, 10)
	rand3 = random.randrange(1, 10)
	rand4 = random.randrange(1, 10)
	rand5 = random.randrange(1, 10)

	# Random operation
	opRand1 = random.choice(ops)
	opRand2 = random.choice(ops)
	opRand3 = random.choice(ops)
	opRand4 = random.choice(ops)

	math = str(rand1) + opRand1 + str(rand2) + opRand2 + str(rand3) + opRand3 + str(rand4) + opRand4 + str(rand5)
	return math

def validateQuestion(userAnswer, math):
	answer = eval(math)
	acceptableAnswer = convertFloat(userAnswer)

	if not acceptableAnswer:
		return False
	
	finalUserAnswer = round(float(userAnswer), 2)
	finalAnswer = round(float(answer), 2)
	
	if finalUserAnswer == finalAnswer:
		return True
	else:
		return False

def calculateScore(remainTime):
	score = 10 * (remainTime/30)
	finalScore = round(score, 2)
	return finalScore
