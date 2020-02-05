import random
def hit(srate):
    roll = random.randint(0, 50)
    if roll <= srate:
        print('You hit successful')
        enemyhp()
    else:
        print('You missed the hit')
def myhpo():
    global hpo1
    damage=random.randint(1,10)
    hpo1=hpo1-damage
    print('Enemy made', damage, 'damage to you')
    print('You have hp', hpo1)

def enemyhpo():
        global hpo2
        damage2 = random.randint(1, 10)
        hpo2 = hpo2 - damage2
        hpo2 = 0
        print('You made', damage2, 'damage to you')
        print('Enemy have hp', hpo2)
def playerhpo():
    global hpo1
    damage1=random.randint(1,10)
    hpo1=hpo1-damage1
    hpo1=0
    print('You made', damage1, 'damage to you')
    print('Enemy have hp', hpo1)

hpo1=40
hpo2=35
y=1
try:
    while y==1:
        print('You are facing a strong enemy!')
        choice = input('choose attack\n a.Meteor shower attack\n b.volt-wave \n c.Melee attacks\n')
        if choice == 'a':
            print('You use Meteor shower successfully attack the enemy')
            hit(10)
            playerhpo()
        elif choice == 'b':
            print('You use Meteor shower successfully attack the enemy')
            hit(15)
            playerhpo()
        elif choice == 'c':
            print('You use Melee attacks successfully hit the enemy')
            hit(20)
            playerhpo()
    while True:
         if hpo2 <= 0:
            print('You win the bottle!')
            choice2 = input('Do you want to play again? yes\n no\n')
         if choice2 == 'no':
            y = 0
            break
         elif choice2 == 'yes':
            break
         elif hpo1 <= 0:
             print('You loss the bottle :/')
         elif choice3 == 'yes':
             break
    choice = input()
except:
    print('Oops, something goes wrong'

          banana='1'
        if banana="hi"
        print('hi')
        else:
        print('hello')