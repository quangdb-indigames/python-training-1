import gameFunctions
import time

# Game start part
welcomeLine = """\n
****************************
* WELCOME TO THE QUIZ GAME *
****************************\n"""
print(welcomeLine)
totalRound = 3
name = input("What is your name? ")
rule = """\n Let's say the rule:
- Have total """ + str(totalRound) + """ questions
- You have 30s for answer question
- If the answer is float, round it to 2~3 decimals
- Press n to skip question
- Score calculate according to the answer and timer
- At the end of game, you can select to keep playing or stop
That's all. Have Fun!!\n"""
print(rule)
input(" Press when you ready! ")
cont_play = True
round = 0
totalScore = 0

# Game main loop
while cont_play == True:
    round += 1

    print("\nRound ", round)
    quiz = gameFunctions.randomQuestion()
    print("Your question is: ", quiz)
    start_time = time.time()

    userAnswer = input("Your answer is: ")
    remainTime = 30 - (time.time() - start_time)

    if (userAnswer == "n" or remainTime < 0) and round < totalRound:
        # If isnt last round, skip to next question
        print("Time runout or skip question, move to next question")
        continue
    elif (userAnswer == "n" or remainTime < 0) and round == totalRound:
        # If last round, run the endgame logic
        print("You have done all question")
        gameFunctions.updateUserPoints(name, totalScore)
        print("===========Leader Board============\n")
        gameFunctions.showLeaderBoard()
        print("===================================\n")
        ans = input("Do you want to continue? y or n: ")
        if ans == "y":
            round = 0
            totalScore = 0
            continue
        else:
            cont_play = False
    else:
        correct = gameFunctions.validateQuestion(userAnswer, quiz)
        if correct == True:
            roundScore = gameFunctions.calculateScore(remainTime)
            totalScore += roundScore
            print("Your answer is true, you get: ", roundScore, " score")
        else:
            print("Your answer is wrong or not in acceptable form")
    
    #Endgame logic
    if round == totalRound:
        print("\nYou have done all question!!\n")
        gameFunctions.updateUserPoints(name, totalScore)
        print("===========Leader Board============\n")
        gameFunctions.showLeaderBoard()
        print("===================================\n")
        ans = input("Do you want to continue? y or n: ")
        if ans == "y":
            round = 0
            totalScore = 0
            continue
        else:
            cont_play = False
    
