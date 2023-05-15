import time
import random
print("Simulation of dice:")
rollchoice =  str(input("Would you like to roll the dice(y/n) :"))
while rollchoice == 'y':
    dicenum = random.randint(1,6)
    print("Rollin the dice..............")
    time.sleep(3)
    print("The number is ",dicenum)
    rollchoice =  str(input("Would you like to roll the dice again(y/n) :"))


    
