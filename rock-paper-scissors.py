'''
RULES :: 
for rock = press 'r'
for scissor = press 's'
for paper = press 'p'
to end the current game = press 'e'
'''

import turtle
import random
import time
import os


#turtle screen setup
def screen_setup():
        scrn = turtle.Screen()
        scrn.bgcolor("#A4E4F2")
        scrn.title("Rock-Paper-Scissor")
        scrn.setup(height=600,width = 700)
        
        



#creating portion for player and computer
def split_screen() :
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.setposition(0,-300)
        t.pendown()
        t.hideturtle()
        t.color("#01041F")
        t.pensize(3)
        t.left(90)
        t.forward(600)

def player_enviroment() :
        
        you.shape(paper_image)
        you.penup()
        you.speed(0)
        you.goto(-175,0)
        


def computer_enviroment() :
        
        comp.shape(paper_image)
        comp.speed(0)
        comp.penup()
        comp.goto(175,0)

def computer_move(c) :

        idx = random.randint(1,1000) % 3
        global score_you
        global score_comp 
        if idx!=c :
                #rock paper
                if c==0 and idx==1 : score_comp+=1
                elif c==1 and idx==1 : score_you+=1
                #rock scissor
                elif c==0 and idx==2 : score_you+=1
                elif c==2 and idx==0 : score_comp+=1
                # paper scissor
                elif c==1 and idx==2 : score_comp+=1
                elif c==2 and idx==1 : score_you+=1
                
        comp.shape(images[idx])
        peny.clear()
        peny.write(f"You: {score_you}",align="center", font = ("Comic Sans MS",22))

        penc.clear()
        
        penc.write(f"Computer: {score_comp}",align="center", font = ("Comic Sans MS",22))

def rock() :
        you.shape(rock_image)
        computer_move(0)

        


def paper() :
        you.shape(paper_image)
        computer_move(1)


def scissor():
        you.shape(scissor_image)
        computer_move(2)


def take_input() :
        kb = turtle.Screen()
        kb.listen()
        kb.onkey(rock,"r")
        kb.onkey(paper,"p")
        kb.onkey(scissor,"s")
        kb.onkey(end,"e")


def end() :
   turtle.clearscreen()
   turtle.bgcolor("#F1B28E")
   sp = turtle.Turtle()
   sp.hideturtle()
   sp.color("#0B17BF")
   if(score_comp>score_you) : sp.write("computer won!!",align="center", font = ("Comic Sans MS",30))
   elif (score_comp<score_you) : sp.write("You won!!",align="center", font = ("Comic Sans MS",30))
   else : sp.write("Draw",align="center", font = ("Comic Sans MS",30))
   time.sleep(2)
   turtle.bye()      
       


#variables 
you = turtle.Turtle()
comp = turtle.Turtle()
peny = turtle.Turtle()
penc = turtle.Turtle()

#worksteps
screen_setup()
split_screen()

# image define 
rock_image= 'rock.gif'
paper_image = 'paper.gif'
scissor_image = 'scissors.gif'
images = [rock_image,paper_image,scissor_image]



turtle.register_shape(rock_image)
turtle.register_shape(paper_image)
turtle.register_shape(scissor_image)



player_enviroment()
computer_enviroment()

take_input()

score_you = 0
score_comp = 0

#initial score

peny.speed(0)
peny.penup()
peny.hideturtle()
peny.goto(-160,180)
peny.color("#390395")
peny.write("You : 0", align="center", font = ("Comic Sans MS",22))


penc.speed(0)
penc.penup()
penc.hideturtle()
penc.goto(160,180)
penc.color("#390395")
penc.write("Computer : 0", align="center", font = ("Comic Sans MS",20))

input("Press any key to exit ...")










