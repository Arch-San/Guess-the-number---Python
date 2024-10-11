import random
randNum = random.randint(1,100) 
while(True):
    userNum = input("Guess the number(1 to 100) or quit(Q) ")
    if(userNum == 'Q' or userNum == 'q'):
        break
    if(userNum.isnumeric()):
        userNum = int(userNum)
        if(userNum == randNum):
            print("The no is ",randNum," You guessed it right!\n")
            break
        elif(userNum < randNum):
            print("Number you entered is < the target number\n")
        else:
            print("Number you entered is > the target number\n")
    else:
        print("Invalid value entered!\n")

print("***GAME OVER***")