from msilib.schema import Icon
from turtle import title
import pgzrun
from time import time
from random import randint
import os


infotext = [""]
swordlaunching = ["False"]
highscore = [0]
swordvel = [0]
if os.path.exists('score.txt'):
    with open ('score.txt', 'r') as file:
        highscore[0] = int(file.read())
score = [0]
moveleft = "false"
moveright = "false"
HEIGHT = 470
WIDTH = 800
apple = Actor("apple")
sword = Actor("sword")
def draw():
    screen.fill((85,255,23)) 
    apple.draw()
    sword.draw()
    screen.draw.rect(Rect((0, 0), (800, 45)), (0, 0, 0))
    screen.draw.text("score: " + str(score[0]), (20, 5), color=(255, 255, 255))
    screen.draw.text("highscore: " + str(highscore[0]), (20, 25), color=(255, 255, 255))
    screen.draw.text(infotext[0], (400, 25), color=(255, 255, 255))

def place_apple():
    apple.x = randint(10,800)
    apple.y = 70

place_apple()

TITLE = "Shoot the apple"

def place_sword():
    sword.y = 450
    sword.x = 400

place_sword()

def timesup():
    infotext[0] = "Time is up! You had a score of " + str(score[0])
    if swordlaunching[0] == "True":
        swordlaunching[0] = "False"
    place_sword()
    score[0] = 0


def hitormiss():
    if apple.collidepoint(sword.x, apple.y):
        infotext[0] = "Nice shot!"
        place_apple()
        score[0] += 1
        if score[0] > highscore[0]:
            highscore[0] = score[0]
            with open('score.txt', 'w') as file:
                file.write(str(highscore[0]))
    else:
        infotext[0] = "You missed!"
        place_apple()

def update():
    if swordvel[0] > 0:
        if swordvel[0] < 0.1:
            swordvel[0] = 0
        swordvel[0] -= 0.1
    if swordvel[0] < 0:
        swordvel[0] += 0.1
    sword.x += swordvel[0]
    
    if swordvel[0] > 10:
        swordvel[0] = 10
    if swordvel[0] < -10:
        swordvel[0] = -10
    
    if sword.x < 10:
        sword.x = 10
        swordvel[0] = 0-swordvel[0]
    if sword.x > 790:
        sword.x = 790
        swordvel[0] = 0-swordvel[0]

    if sword.y < 80:
        sword.y = 450
        swordlaunching[0] = "False"

    if sword.y == 80:
        hitormiss()
    
    if swordlaunching[0] == "True":
        sword.y -= 5

    if keyboard.left:
        if swordlaunching[0] == "False":
            swordvel[0] -= 0.2
    if keyboard.right:
        if swordlaunching[0] == "False":
            swordvel[0] += 0.2
    if keyboard.space:
        if swordlaunching[0] == "False":
            swordlaunching[0] = "True"
clock.schedule(timesup, 12.0)
pgzrun.go()