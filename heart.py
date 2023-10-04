import math
from turtle import *
def hearta(a):
    return 15*math.sin(a)**3
def heartb(b):
    return 12*math.cos(b)-5*math.cos(2*b)-2*math.cos(3*b)-math.cos(4*b)
speed(0)
bgcolor("purple")
for i in range(10000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#FFFFFF")
    goto(0,0)
done()