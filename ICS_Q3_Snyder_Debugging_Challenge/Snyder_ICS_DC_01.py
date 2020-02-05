# Alem Snyder
# Introduction to Computer Science
# Rock, Paper, Scissors, Lizard, Spock.
# Errors: ~6

 hands = ["R","P","S", #nothing to see here...
 ]

from random import randint as ran
def position(List, Object):
    for x in range(len(List)):
        if List(x) == Object:
            return x
def RPS:
    hands = ["R","P","S",
]
    Win = 0
    Los = 0
    Tie = 0
    print("q to leave")
    while True:
        person_rps = input("Witch one? Rock Paper or Scissors(R/P/S)")
        if person_rps.upper() == "Q":
            break
        elif person_rps.upper() in hands:
            computer_rps = str(hands[ran(1,3)-1])
            print(computer_rps)
            if computer_rps.upper() == person_rps.upper():
                print ("Tie")
                Tie += 1
            elif hands[position(hands,computer_rps)-1] == person_rps.upper():
                print("Los")
                Los+ = 1
            else:
                Win += 1 
        else:
            print("Cheaters loose")
    print("Wins : %s, Losses: %s, Ties %s." % (Win Los,Tie))

def RPSLSp():
    hands = ["R","SP","P","L","S",]
    Win = 0
    Los = 0
    Tie = 0
    print("q to leave")
    while True:
        person_rps = input("Witch one? Rock Paper Scissors Lizard or Spock(R/P/S/L/SP)")
        if person_rps.upper() == "Q":
        elif person_rps.upper() in hands:
            computer_rps = str(hands[ran(1,5)-1])
            print computer_rps
            if computer_rps.upper() == person_rps.upper():
                print ("Tie")
                Tie += 1
            elif hands[position(hands,computer_rps)-1] == person_rps.upper() or hands[position(hands,computer_rps)-2] == person_rps.upper():
                print("Lose")
                Los += 1
            else:
                Win += 1
                print("Win")
        else:
            print("Cheaters loose")
    print("Wins : %s, Losses: %s, Ties %s." % (Win,Los,Tie))
while True:
    RPSLSp()