#Added "wait" function before displaying the next question: 19/03/2017

#imports python pre-defined functions

import csv
from sys import exit
import time

def scoreboard(info):
     with open('D:\\Advanced Higher Computing\\WHO WANTS TO BE A MILLIONAIRE PROJECT\\ADVH Computing Project\\solution files\\scorelist.csv','a+') as sfile:
            sfile.write('\n')
            sfile.write(info)

     readandsort()
def winner(username):
    
    
    #special function reserved for the winner, does exactly the same as above but with a 'WINNER' message at the end#
    

    ## display error encountered: 19:25
    ## display error fixed: 

    winnerinfo = ('10,%s,£1000000' %username)

    with open('D:\\Advanced Higher Computing\\WHO WANTS TO BE A MILLIONAIRE PROJECT\\ADVH Computing Project\\solution files\\scorelist.csv','a+') as sfile:
        sfile.write('\n')
        sfile.write(winnerinfo)
    
def start():
    
    #opens and reads a file containing questions and answers#
    
    temp = []
    QUESTION = []
    ANSWER = []
        
    file = open('D:\\Advanced Higher Computing\\WHO WANTS TO BE A MILLIONAIRE PROJECT\\ADVH Computing Project\\solution files\\questionlist.csv','r')
    for line in file:
        data = line
        question,answer = data.split(',')
        QUESTION.append(question)
        ANSWER.append(answer)
    temp.append(QUESTION)
    temp.append(ANSWER)

    
        



    #assigning rows of the file to certain variables#
    
    q1 =[]
    q2 =[]
    q3 =[]
    q4 =[]
    q5 =[]
    q6 =[]
    q7 =[]
    q8 =[]
    q9 =[]
    q10 =[]
    
    q1.append(temp[0][0])
    q2.append(temp[0][1])
    q3.append(temp[0][2])
    q4.append(temp[0][3])
    q5.append(temp[0][4])
    q6.append(temp[0][5])
    q7.append(temp[0][6])
    q8.append(temp[0][7])
    q9.append(temp[0][8])
    q10.append(temp[0][9])

    q1.append(temp[1][0])
    q2.append(temp[1][1])
    q3.append(temp[1][2])
    q4.append(temp[1][3])
    q5.append(temp[1][4])
    q6.append(temp[1][5])
    q7.append(temp[1][6])
    q8.append(temp[1][7])
    q9.append(temp[1][8])
    q10.append(temp[1][9])

    
    print("""================================================================================
                     WHO WANTS TO BE A MILLIONAIRE?
================================================================================ """)

    
    #Game start, asking for the user's desired username#
    
    valid = False
    while valid is False:
        username=input("Enter your desired username: ")
        if username == "":
            print("Please enter a valid username")
        else:
    
            print("Hello %s, Welcome to Who wants to be a Millionaire (not literally because I would lose money). Are you ready to play (yes or no)? " %username)
    
            present = False

            while present is False:
                choice = input("> ")
                if choice == "yes":
                    questionone(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username)
                elif choice == "no":
                    print("See you next time on Who wants to be a millionaire!")
                    exit(0)
                else:
                    print("I cannot interpret your input")

            

#The next 10 functions ask different questions, each containing the following                  #
#baseprize = "Prize" that the player takes home                                                #
#level = the current level that the player is answering                                        #
#"info = ('%s,%s,%s' %(level,username,baseprize))" -> assigns print format to variable "info"  #


def questionone(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username):
    baseprize = "£00.00"
    level = "0"
    info = ('%s,%s,%s' %(level,username,baseprize))
    
    print("------------" *20)
    print("Question 1: For £500.00, answer the question")
    print("%s. %s" % (q1[0], q1[1]))

    correct = False
    
    ## validation error encountered: 10/03/17
    ## validation error fixed 12/03/17
    while correct is False:
        aq1 = input("Your answer:  ")
        if aq1 == "a":
            print("Congratulations! You have won £500.00 (virtual money). You will now move on to the second question")
            time.sleep(2)
            questiontwo(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username)
        elif aq1 == "b":
            print("You lose without taking home anything. YOU SUCK")
            scoreboard(info)
        elif aq1 == "c":
            print("You lose without taking home anything. YOU SUCK")
            scoreboard(info)
        elif aq1 == "d":
            print("You lose without taking home anything. YOU SUCK")
            scoreboard(info)
        else:
            print("Please enter a valid answer")

def questiontwo(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username):
    baseprize = "£00.00"
    level = "1"
    info = ('%s,%s,%s' %(level,username,baseprize))

    print("------------" *20)
    print("Question 2: For £1000.00, answer the question")
    print("%s. %s" % (q2[0], q2[1]))

    correct = False
    while correct is False:
        aq2 = input("Your answer:  ")
    
        if aq2 == "a":
            print("Congratulations! You have won £1000.00. You will now move on to the third question")
            time.sleep(2)
            questionthree(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username)
        elif aq2 == "b":
            print("You lose without taking home anything. YOU SUCK")
            scoreboard(info)
        elif aq2 == "c":
            print("You lose without taking home anything. YOU SUCK")
            scoreboard(info)
        elif aq2 == "d":
            print("You lose without taking home anything. YOU SUCK")
            scoreboard(info)
        else:
            print("Please enter a valid answer")

def questionthree(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username):
    baseprize = "£1000.00"
    level = "2"
    info = ('%s,%s,%s' %(level,username,baseprize))
    
    print("------------" *20)
    print("Question 3: For £2000.00, answer the question")
    print("%s. %s" % (q3[0], q3[1]))

    correct = False

    while correct is False:
        aq3 = input("Your answer:  ")
    
        if aq3 == "a":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        elif aq3 == "b":
            print("Congratulations! You have won £2000.00. You will now move on to the fourth question")
            time.sleep(2)
            questionfour(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username)
        elif aq3 == "c":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        elif aq3 == "d":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        else:
            print("Please enter a valid answer")

def questionfour(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username):
    baseprize = "£1000.00"
    level = "3"
    info = ('%s,%s,%s' %(level,username,baseprize))

    print("------------" *20)
    print("Question 4: For £10000.00, answer the question")
    print("%s. %s" % (q4[0], q4[1]))

    correct = False
    while correct is False:
        aq4 = input("Your answer:  ")
    
        if aq4 == "a":
            print("Congratulations! You have won £10000.00. You will now move on to the fifth question")
            time.sleep(2)
            questionfive(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username)
        elif aq4 == "b":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        elif aq4 == "c":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        elif aq4 == "d":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        else:
            print("Please enter a valid answer")

def questionfive(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username):
    baseprize = "£1000.00"
    level = "4"
    info = ('%s,%s,%s' %(level,username,baseprize))

    print("------------" *20)
    print("Question 5: For £20000.00, answer the question")
    print("%s. %s" % (q5[0], q5[1]))
    correct = False
    while correct is False:
        aq5 = input("Your answer:  ")
    
        if aq5 == "a":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        elif aq5 == "b":
            print("Congratulations! You have won £20000.00. You will now move on to the sixth question")
            time.sleep(2)
            questionsix(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username)
        elif aq5 == "c":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        elif aq5 == "d":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        else:
            print("Please enter a valid answer")

def questionsix(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username):
    baseprize = "£1000.00"
    level = "5"
    info = ('%s,%s,%s' %(level,username,baseprize))

    print("------------" *20)
    print("Question 6: For £50000.00, answer the question")
    print("%s. %s" % (q6[0], q6[1]))

    correct = False
    while correct is False:
        aq6 = input("Your answer:  ")
    
        if aq6 == "a":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        elif aq6 == "b":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        elif aq6 == "c":
            print("You go home taking £1000.00 with you")
            scoreboard(info)
        elif aq6 == "d":
            print("Congratulations! You have won £50000.00. You will now move on to the seventh question")
            time.sleep(2)
            questionseven(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username)
        else:
            print("Please enter a valid answer")

def questionseven(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username):
    baseprize = "£50000.00"
    level = "6"
    info = ('%s,%s,%s' %(level,username,baseprize))

    print("------------" *20)
    print("Question 7: For £100000.00, answer the question")
    print("%s. %s" % (q7[0], q7[1]))

    correct = False
    while correct is False:
        aq7 = input("Your answer:  ")
    
        if aq7 == "a":
            print("You go home taking £50000.00 with you")
            scoreboard(info)
        elif aq7 == "b":
            print("Congratulations! You have won £10000.00. You will now move on to the eighth question")
            time.sleep(2)
            questioneight(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username)
        elif aq7 == "c":
            print("You go home taking £50000.00 with you")
            scoreboard(info)
        elif aq7 == "d":
            print("You go home taking £50000.00 with you")
            scoreboard(info)
        else:
            print("Please enter a valid answer")
def questioneight(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username):
    baseprize = "£50000.00"
    level = "7"
    info = ('%s,%s,%s' %(level,username,baseprize))

    print("------------" *20)
    print("Question 8: For £250000.00, answer the question")
    print("%s. %s" % (q8[0], q8[1]))
    correct = False
    while correct is False:
        aq8 = input("Your answer:  ")
    
        if aq8 == "a":
            print("You go home taking £50000.00 with you")
            scoreboard(info)
        elif aq8 == "b":
            scoreboard(info)
        elif aq8 == "c":
            print("Congratulations! You have won £250000.00. You will now move on to the nineth question")
            time.sleep(2)
            questionnine(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username)
        elif aq8 == "d":
            print("You go home taking £50000.00 with you")
            scoreboard(info)
        else:
            print("Please enter a valid answer")

def questionnine(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,username):
    baseprize = "£50000.00"
    level = "8"
    info = ('%s,%s,%s' %(level,username,baseprize))

    print("------------" *20)
    print("Question 9: For £500000.00, answer the question")
    print("%s. %s" % (q9[0], q9[1]))
    
    correct = False
    while correct is False:
        aq9 = input("Your answer:  ")
    
        if aq9 == "a":
            print("Congratulations! You have won £250000.00. You will now move on to the tenth question")
            time.sleep(2)
            questionten(q10,username)
        elif aq9 == "b":
            scoreboard(info)
        elif aq9 == "c":
            print("You go home taking £50000.00 with you")
            scoreboard(info)
        elif aq9 == "d":
            print("You go home taking £50000.00 with you")
            scoreboard(info)
        else:
            print("Please enter a valid answer")

def questionten(q10,username):
    baseprize = "£250000.00"
    level = "9"
    info = ('%s,%s,%s' %(level,username,baseprize))

    print("------------" *20)
    print("Question 10: For £1000000.00, answer the question")
    print("%s. %s" % (q10[0], q10[1]))

    correct = False
    while correct is False:
        aq10 = input("Your answer:  ")
    
        if aq10 == "a":
            print("You go home taking £250000.00 with you")
            scoreboard(info)
        elif aq10 == "b":
            print("You go home taking £250000.00 with you")
            scoreboard(info)
        elif aq10 == "c":
            print("Congratulations! You have won £1000000.00. You will go down in Who wants to be a millionaire history!")
            #special function to denote winner
            winner(username)
            #starts to display leaderboard 
            readandsort()
        elif aq10 == "d":
            print("You go home taking £250000.00 with you")
            scoreboard(info) 
        else:
            print("Please enter a valid answer")



def readandsort():
    #opens the csv file containing the unsorted data list and puts it in a python list
    file = open('D:\\Advanced Higher Computing\\WHO WANTS TO BE A MILLIONAIRE PROJECT\\ADVH Computing Project\\solution files\\scorelist.csv','r')
    ls = list(file)

    #insertion sort to sort the data in descending order [from highest achieved level to lowest achieved level]
    for index in range(1, len(ls)): 
        value = ls[index] 
        pos = index - 1 
 
        while pos >= 0 and ls[pos] < value: 
            ls[pos+ 1] = ls[pos] 
            pos = pos - 1 
        ls[pos+1] = value

## write error encountered: 17:30 13/02/17
## write error fixed: 17:57 14/02/17
    with open('D:\\Advanced Higher Computing\\WHO WANTS TO BE A MILLIONAIRE PROJECT\\ADVH Computing Project\\solution files\\leaderboard.txt', mode='w', encoding='utf-8') as wfile:
        wfile.write("".join(map(lambda x: str(x),ls)))

    time.sleep(2)

    leaderboard()
## read error encountered: 17:58 14/02/17
## read error fixed: 17:59 14/02/17

def leaderboard():
     #reads the sorted score data and displays it ingame
    file = open('D:\\Advanced Higher Computing\\WHO WANTS TO BE A MILLIONAIRE PROJECT\\ADVH Computing Project\\solution files\\leaderboard.txt',mode='r', encoding='utf-8')
    reader = file.read()
    print("-" *20)
    print("Leaders [level, username, prize money]")
    print(reader)

    restart()

def restart():
    ## gives the player a chance to restart the game without clicking the game again
    choice = input("Would you like to restart the game? (yes/no): ")

    if "yes" in choice:
        start()
    elif "no" in choice:
        exit(0)
    else:
        return "I do not know what you are trying to say"
        restart()

    
            
    

start()
