from turtle import *

shape('arrow')
speed(10)

def circulo() :
    for i in range(24) :
        forward(10)
        left(15)

def cuadrado(lado=100) :
    for i in range(4) :
        forward(lado)
        left(90)

def suma(x,y) :
    return x+y

def triangulo(lado) :
    for i in range(3) :
        forward(lado)
        left(120)

def poligono(lados, longitud) :
    for i in range(lados) :
        forward(longitud)
        left(360/lados)

def mult(x, y) :
    for i in range(y-1):
        x = x+y
    return x

    
print (mult(12,12))
