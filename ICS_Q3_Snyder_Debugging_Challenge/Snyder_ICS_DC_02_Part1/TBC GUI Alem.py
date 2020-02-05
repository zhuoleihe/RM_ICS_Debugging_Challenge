# ALem Snyder
# Introduction to Conputer Science
# Tain
# Turned backed combat GUI

#
#
# 180 y
#
#
#############################
#            260 x

# import all the things
import tkinter as tk
from random import randint
from tkinter import messagebox
import time

def OpenImg(Name,x,y,n=1): # define a function that opens an image and makes it y*n by x*n image
    img =  tk.PhotoImage(file=Name)
    img = img.zoom(int(x*n/img.width()),int(y*n/img.height()))
    return img # Returns the image
n = 3 # the globle scaling constant

class Start(tk.Tk): # each page is a frame class the one holed all

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        self.resizable(False, False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (FruntPage, B1,B2,B3, descriptions, WinPage, LossPage):

            frame = F(container, self) # initializes all of the child frames

            self.frames[F] = frame # adds them tall to a directory

            frame.grid(row=0, column=0, sticky="nsew") # places them

        self.show_frame(FruntPage) # show the first page

    def show_frame(self, cont): # rases the input frame

        frame = self.frames[cont]
        frame.tkraise()
        
class FruntPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        # make a cnavas with the background image
        canvas = tk.Canvas(self, width = 260*n, height = 180*n,highlightthickness=0)
        canvas.pack()
        self.imgFrountPage = OpenImg("Front.gif",260,180,n)
        canvas.create_image(0,0, anchor = tk.NW, image = self.imgFrountPage)
        
        # the three butons take you to each battle
        self.Fight1img = OpenImg("B1start.gif",55,80,n)
        buttonFight1 = tk.Button(self,borderwidth = 0,image = self.Fight1img, highlightthickness = 0, bd = 0, command=lambda: controller.show_frame(B1))
        buttonFight1.place(x=10*n,y=125*n,anchor = tk.SW)
        buttonFight2 = tk.Button(self,borderwidth = 0,image = self.Fight1img, highlightthickness = 0, bd = 0, command=lambda: controller.show_frame(B2))
        buttonFight2.place(x=130*n,y=125*n,anchor = tk.S)
        buttonFight3 = tk.Button(self,borderwidth = 0,image = self.Fight1img, highlightthickness = 0, bd = 0, command=lambda: controller.show_frame(B3))
        buttonFight3.place(x=250*n,y=125*n,anchor = tk.SE)

class WinPage(tk.Frame): # a page with one button that runs when you win

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        canvas = tk.Canvas(self, width = 260*n, height = 180*n,highlightthickness=0)
        canvas.pack()
        
        # the button covers the canvas and takes you back to the first page
        self.buttonimg = OpenImg("Win.gif", 260, 180, n)
        buttonGoback = tk.Button(self,borderwidth = 0,image = self.buttonimg, highlightthickness = 0, bd = 0, command=lambda: controller.show_frame(FruntPage))
        buttonGoback.place(x=0,y=0,anchor = tk.NW)
        
class LossPage(tk.Frame): # it's the same but with a different image

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        canvas = tk.Canvas(self, width = 260*n, height = 180*n,highlightthickness=0)
        canvas.pack()
        self.buttonimg = OpenImg("Lose.gif", 260, 180, n)
        buttonGoback = tk.Button(self,borderwidth = 0,image = self.buttonimg, highlightthickness = 0, bd = 0, command=lambda: controller.show_frame(FruntPage))
        buttonGoback.place(x=0,y=0,anchor = tk.NW)
        
class Battle(tk.Frame): # the generalized battle class. it only wokes for one enemy though
    
    def __init__(self, parent, controller, BG):
        
        self.Con=controller # I needed to call that somewher elce
        tk.Frame.__init__(self,parent)
        
        
        
        # the hit and miss images that show up. they are first becasue they should be at the bottom
        self.HitImg = OpenImg("Hit.gif",85,50,n)
        self.HitLabel = tk.Label(self,borderwidth = 0,image = self.HitImg, highlightthickness = 0, bd = 0)
        self.HitLabel.place(y = 85*n,x = 130*n,anchor = tk.N)
        
        self.MissImg = OpenImg("Miss.gif",85,50,n)
        self.MissLabel = tk.Label(self,borderwidth = 0,image = self.MissImg, highlightthickness = 0, bd = 0)
        self.MissLabel.place(y = 85*n,x = 130*n,anchor = tk.N)
        
        # The canvas goes on top of the labels
        self.canvas = tk.Canvas(self, width = 260*n, height = 150*n,highlightthickness=0)
        self.canvas.pack()
        
        self.Barkground = OpenImg(BG,260,150,n)
        self.canvas.create_image(0,0, anchor = tk.NW, image = self.Barkground)
        
        buttonB = tk.Button(self,borderwidth = 0,text = "Back", highlightthickness = 0, bd = 0, command=lambda: controller.show_frame(FruntPage))
        buttonB.place(x=0,y=0,anchor = tk.NW)
        
        
        #buttons are 30x by 65y
        
        # the atack and potion butons:
        self.ToPButton = OpenImg("GoToPotions.gif",65,30,n)
        AtPB = tk.Button(self,borderwidth = 0,image = self.ToPButton, highlightthickness = 0, bd = 0,command = self.raiseP)
        AtPB.place(y = 540,x = 0,anchor = tk.SW)
        
        self.AB1P = OpenImg("Atack2.gif",65,30,n)
        AB1 = tk.Button(self,borderwidth = 0,image = self.AB1P, highlightthickness = 0, bd = 0, command = lambda: self.ThePlayer.atack1(self.Enemy))
        AB1.place(y = 180*n,x = 65*n,anchor = tk.SW)
        
        self.AB2P = OpenImg("Atack1.gif",65,30,n)
        AB2 = tk.Button(self,borderwidth = 0,image = self.AB2P, highlightthickness = 0, bd = 0, command = lambda: self.ThePlayer.atack2(self.Enemy))
        AB2.place(y = 180*n,x = 65*n*2,anchor = tk.SW)
        
        self.AB3P = OpenImg("Atack3.gif",65,30,n)
        AB3 = tk.Button(self,borderwidth = 0,image = self.AB3P, highlightthickness = 0, bd = 0,  command = lambda: self.ThePlayer.atack3(self.Enemy))
        AB3.place(y = 180*n,x = 65*n*3,anchor = tk.SW)
        
        self.AButtons = (AB1,AB2,AB3,AtPB) # for self.raiseA/B
        
        self.ToAButton = OpenImg("GoToAtacks.gif",65,30,n)
        PB4 = tk.Button(self,borderwidth = 0,image = self.ToAButton, highlightthickness = 0, bd = 0, command = self.raiseA)
        PB4.place(y = 180*n,x = 0,anchor = tk.SW)
        
        self.PB1P = OpenImg("Potion1.gif",65,30,n)
        PB1 = tk.Button(self,borderwidth = 0,image = self.PB1P, highlightthickness = 0, bd = 0, command = lambda: self.ThePlayer.potion1(self.Enemy))
        PB1.place(y = 180*n,x = 65*n*1,anchor = tk.SW)
        
        self.PB2P = OpenImg("Potion2.gif",65,30,n)
        PB2 = tk.Button(self,borderwidth = 0,image = self.PB2P, highlightthickness = 0, bd = 0, command = lambda: self.ThePlayer.potion2(self.Enemy))
        PB2.place(y = 180*n,x = 65*n*2,anchor = tk.SW)
        
        self.PB3P = OpenImg("Potion3.gif",65,30,n)
        PB3 = tk.Button(self,borderwidth = 0,image = self.PB3P, highlightthickness = 0, bd = 0, command = lambda: self.ThePlayer.potion3(self.Enemy))
        PB3.place(y = 180*n,x = 65*n*3,anchor = tk.SW)
        
        self.PButtons = (PB1,PB2,PB3,PB4)
        
    
        
    def raiseA(self): #switches to the atack butons
        for button in self.AButtons:
            button.tkraise()
    def raiseP(self): # switches to the potion butons
        for button in self.PButtons:
            button.tkraise()
    def BigMiss(self): # shows a large "Miss" sign
        self.MissLabel.tkraise()
        self.update()
        time.sleep(.2)
        tk.Misc.lift(self.canvas, aboveThis=None)
    def BigHit(self): # for when you hit
        self.HitLabel.tkraise()
        self.update() # this waits for tkinter to update then
        time.sleep(.2) # then the program pausses for .2 seconds
        tk.Misc.lift(self.canvas, aboveThis=None) # hides the "Hit" label

# the three battles
# they are so similar even the images are the same
# Photoshop stoped working for me so I could not make more monsters
class B1(Battle):
    def __init__(self, parent, controller):
        Battle.__init__(self, parent, controller,"Fight1.gif",)
        self.Enemy = Monster(self,(140*n,125*n),"bigBad.gif","Big Bad",100,(10,20),"Big Smack")
        self.ThePlayer = Player(self,(20*n,135*n),"Player.gif",100)
        self.raiseA()
        
class B2(Battle):
    def __init__(self, parent, controller):
        Battle.__init__(self, parent, controller,"Fight1.gif",)
        self.Enemy = Monster(self,(140*n,125*n),"bigBad.gif","Big Bad",100,(20,30),"Big Smack")
        self.ThePlayer = Player(self,(20*n,135*n),"Player.gif",100)
        self.raiseA()
class B3(Battle):
    def __init__(self, parent, controller):
        Battle.__init__(self, parent, controller,"Fight1.gif",)
        self.Enemy = Monster(self,(140*n,125*n),"bigBad.gif","Big Bad",100,(40,60),"Big Smack")
        self.ThePlayer = Player(self,(20*n,135*n),"Player.gif",100)
        self.raiseA()
        
class descriptions(tk.Frame): # in theory this would tell you what each thing did, but isen't more fun to figure it out yourself?
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        canvas = tk.Canvas(self, width = 260*n, height = 180*n,highlightthickness=0)
        canvas.pack()
        self.thisMightNotBeHere = OpenImg("GoToPotions.gif",260,180,n)
        canvas.create_image(0,0, anchor = tk.NW, image = self.thisMightNotBeHere)
        
        buttonB = tk.Button(self,borderwidth = 0,text = "Back", highlightthickness = 0, bd = 0, command=lambda: controller.show_frame(FruntPage))
        buttonB.place(x=130*n,y=33*n,anchor = tk.N)

class Stats: # The class is a base class
    def Display(self): # Displays the objct on the screen can run any time something changes
        self.parent.canvas.create_image(self.P[0],self.P[1], anchor = tk.SW, image = self.BoddyImg)
        
        self.parent.canvas.create_image(self.P[0]-5*n,self.P[1]-70*n, anchor = tk.SW, image = self.statsImg)
        hp = self.__HPP()
        if hp > 0: # This is not a death Function
            self.currentHPBar = self.HPBar.zoom(hp,4)
            self.parent.canvas.create_image(self.P[0],self.P[1]-75*n, anchor = tk.SW, image = self.currentHPBar)
        
        postion=0
        for potion in self.Effects:
            #print(potion , self.Effects[potion]["active"])
            if self.Effects[potion]["active"]:
                self.parent.canvas.create_image(self.P[0]+(10+postion)*n,self.P[1]-80*n, anchor = tk.SW, image = self.Effects[potion]["Img"])
                postion += 10*n

    def __init__(self,parent,Positon,BI,health): # Positon is botom west（left）
        self.statsImg = OpenImg("StatsBar.gif", 110, 50,n)
        self.HPBar =  OpenImg("HPBar.gif", 1, 1,n)
        self.BoddyImg = OpenImg(BI, 70,70,n)
        self.P = Positon
        self.parent = parent
        self.__maxHelth = health
        self.HP = health
        # loding up all the values
        self.Display()
        
    def __HPP(self): # hp Percentage for the bar
        return(int((self.HP/self.__maxHelth) * 100))
        
    def takeDamage(self, D):
        self.HP -= D # subtracts from HP
        if self.HP > self.__maxHelth:
            self.HP = self.__maxHelth
        self.Display()
        self.parent.update()
        time.sleep(.3)
        if self.HP<=0: # tests if something is dead
            if messagebox.askyesno(self.OhealthMessage, 'Do want to play again?'):
                self.parent.Con.show_frame(self.OhealthCommand)
            else: root.destroy()
            #self.HP = 100
            return False # as in dead
        else: return True # as in alive
    def resetHP(self): # resest ph to the max I don't think I use this
        self.HP = self.__maxHelth
        self.Display()
    def PotionTimer(self): # for when your potions run out
        for potion in self.Effects: # goes through each potion
            if self.Effects[potion]["active"]: # test if it is active
                self.Effects[potion]["duration"] -= 1 # reduces the duration
            if self.Effects[potion]["duration"] <= 0: # if there is no more time
                self.Effects[potion]["active"] = False # turns off the potion
class Monster(Stats):
    def __init__(self,parent,Positon,BI, name, health,damage, WeponName):
        self.WName = WeponName
        self.name = name
        self.damage = damage
        #                                                               inacuracy                           , weekenss/less damage
        self.Effects={1:{"active" : False, "duration" : 0, "Img":OpenImg("Week.gif", 20,20, n)},2:{"active" : False, "duration" : 0,"Img":OpenImg("Stuck.gif", 20,20, n)}}
        self.defence = 50 # 50% of hitting
        self.OhealthMessage = "You have defeated the Monster!"
        self.OhealthCommand = WinPage
        # when the monster dies the message is desplayed then you go the winning page
        Stats.__init__(self,parent,Positon,BI,health)
    def Turn(self, player): # Deals damage to the player
        self.PotionTimer()
        self.Display() # then waits for you to see it
        self.parent.update()
        time.sleep(.3)
        
        if player.Effects[2]["active"]: # the secend effect causses a defences bonous
            bonus = 20
        else: bonus = 0
        if self.Effects[1]["active"]: # the sward is broken vary unlikely to hit
            bonus += 40
        if randint(1,100) > player.defence+bonus:
            
            if self.Effects[2]["active"]: # this one is weekness
                bonus = 10
            else: bonus = 0
            D = randint(self.damage[0], self.damage[1]) - bonus
            #print("Hit!\n"+self.name +" used "+self.WName+" and delt "+str(D)+" Damage.")
            self.parent.BigHit() # shows that there is a hit
            player.takeDamage(D) # deals damage to the player
        else:
            #print("Miss!")
            self.parent.BigMiss() # shows that there is a Miss
        self.parent.update() # wait
        time.sleep(.3) # and show
            
class Player(Stats):
    def EndTurn(self, Monster):
        # this runs for each atack
        if self.Effects[1]["active"]: # gain 10 health if you have the first potion
            self.takeDamage(-10)
            self.parent.update()
            time.sleep(.2)
        self.PotionTimer() # general updating stuf
        self.Display()
        self.parent.update()
        time.sleep(.3)
        # it is time for the monster
        Monster.Turn(self)
        
    def atack1(self, mon):
        if self.Effects[3]["active"]: #bones to hit
            bonus = 20
        else: bonus = 0
        if randint(1,100) +30+bonus > mon.defence: # defalt + 30% to hit
            self.parent.BigHit() # displays the hit
            #print("Hit!")
            mon.Effects[1]["active"] = True # less likley it hit
            mon.Effects[1]["duration"] = 3 # gives the monster negitave effects
            MonsterAlive = mon.takeDamage(4) # deals a small amount of damage but the effect is vary strong
            if MonsterAlive: # don't have the monster atack if it is dead
                self.EndTurn(mon)
        else:
            self.parent.BigMiss()
            #print("Miss!")
        # run monster atack
            self.EndTurn(mon)
    def atack2(self, mon):
        if self.Effects[3]["active"]: #bones to hit
            bonus = 20
        else: bonus = 0
        if randint(1,100) +20+bonus > mon.defence:
            #print("Hit!")
            self.parent.BigHit() # displays the hit
            mon.Effects[2]["active"] = True # the monster is weeker
            mon.Effects[2]["duration"] = 3
            MonsterAlive = mon.takeDamage(8)
            if MonsterAlive:
                self.EndTurn(mon)
        else:
            self.parent.BigMiss()
            #print("Miss!")
        
            self.EndTurn(mon)# run monster atack
            
    def atack3(self, mon):
        if self.Effects[3]["active"]: #bones to hit
            bonus = 20
        else: bonus = 0
        if randint(1,100) + bonus > mon.defence:
            #print("Hit!")
            self.parent.BigHit()
            MonsterAlive = mon.takeDamage(20)
            if MonsterAlive:
                self.EndTurn(mon)
        else:
            self.parent.BigMiss()
            #print("Miss!")
        # run monster atack
            self.EndTurn(mon)
        
    def potion1(self, mon): # when using a potions
        self.Effects[1]["active"] = True # turn it on, this one is healing
        self.Effects[1]["duration"] = 3 # and set how long it lasts
        self.EndTurn(mon) # then end you turn
    def potion2(self, mon):
        self.Effects[2]["active"] = True # bonus to defence
        self.Effects[2]["duration"] = 3
        self.EndTurn(mon)
    def potion3(self, mon):
        self.Effects[3]["active"] = True # a bonus to hit
        self.Effects[3]["duration"] = 3
        self.EndTurn(mon)
        
    def __init__(self,parent,Positon,BI,health):
        #                                                   health regen                         , defence                                                                     , bones to hit
        self.Effects={1:{"active" : False, "duration" : 0, "Img":OpenImg("Healing.gif", 20,20, n)},2:{"active" : False, "duration" : 0, "Img":OpenImg("Defence.gif", 20,20, n)},3:{"active" : False, "duration" : 0, "Img":OpenImg("Accurate.gif", 20,20, n)}}
        Stats.__init__(self,parent,Positon,BI,health)
        self.OhealthMessage = "The monster has defeated You!"
        self.OhealthCommand = LossPage
        self.defence = 50 # sets you hit chance, If I had more time this would be defined by an input
root = Start() # like wraing root = tk.Tk()
root.mainloop()# Time to start!
