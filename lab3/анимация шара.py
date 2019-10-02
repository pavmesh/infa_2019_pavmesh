# -*- coding: utf-8 -*-

from graph import *
time=0
dt=50

def func():
    global time
    drawBG()
    shar()
    time+=dt

V_y = 0.2
V_x = 0
y0 = 100
def shar():
    global time
    global V_y
    global V_x
    global y0
    brushColor('green')
    x = 200
    R = 30
    y =y0 + time*V_y
    if y>300 or y<100:
        V_y=-V_y
        y0=400-y0
        time=0
    circle (x,y,R)
    
def drawBG():
    brushColor(140,140,140)
    rectangle(0,0,1000,1000)

onTimer (func,dt)
run()
