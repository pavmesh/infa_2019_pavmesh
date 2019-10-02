from graph import *
from typing import Any
'''
фон
'''
penColor('purple')
rectangle(0, 0, 500, 400)
brushColor(204, 255, 255)
rectangle(0, 0, 500, 200)
brushColor(0, 0, 102)
rectangle(0, 200, 500, 300)
penColor(255, 204, 0)
brushColor(255, 204, 0)
circle(400, 100, 50)
rectangle(0, 300, 500, 400)

'''
круги внизу
'''
n = 13
r = 500 / (n * 2)
x = r
for i in range(n):
    circle(x, 310, r)
    x += 2 * r
'''
корабль 1 2
'''
from math import cos, pi, sin

pol_1=[]
pol_2=[]
i=1
t=0
'''
тело
'''
penColor('brown')
brushColor('brown')
while t !=pi/2:
    t = i / 200 * pi
    dx1 = 250 - 30 * cos(t)
    dy1 = 220 + 30 * sin(t)
    pol_1.append((dx1, dy1))
    
    dx2 = 160 - 30 * cos(t)
    dy2 = 190 + 30 * sin(t)
    pol_2.append((dx2, dy2))
    i+=1

polygon(pol_1)
polygon(pol_2)
polygon([(250,250),(350,250),(420,220),(220,220)])
polygon([(150,220),(200,220),(235,190),(130,190)])

'''
парус
'''
penSize(5)
penColor(50,0,0)
line(295,220,295,120)
line(195,190,195,130)
penSize (2)
brushColor(200,200,200)

polygon([(295,220),(390,170),(320,170),(295,220)])
polygon([(295,120),(390,170),(320,170),(295,120)])
polygon([(195,190),(240,160),(210,160),(195,190)])
polygon([(195,130),(240,160),(210,160),(195,130)])

circle(356,235,9)
circle(210,200,5)
x=100
y=70

'''
зонтик 1 2
'''
penColor(102, 51, 0)
penSize(5)
line(55, 280, 55, 390)
line(205, 250, 205, 390)
brushColor(255, 69, 0)
penSize(1)
polygon([(5, 280), (55, 260), (60, 260), (110, 280)])
polygon([(135, 250), (205, 230), (210, 230), (280, 250)])

brushColor(128, 0, 0)
penColor(128, 0, 0)

'''
облака
'''
penSize(1)
penColor(0,0,240)
brushColor(240,240,240)
r=140
g=140
b=140
for i in range (3):
    circle(x,y,15)
    x+=15
y+=12
x+=-20
for i in range(2):
    circle(x,y,12)
    x-=15


for i in range (10):
    circle(x,y,15+i)
    x+=55-i

y+=22
x+=-60
for i in range(2):
    circle(x,y,12)
    x+=35
run()
