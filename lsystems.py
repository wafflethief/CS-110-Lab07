import turtle
import random

"""
Splits each item in the rules list and return the rule that matches the char given
param list: (char) char, (list) rules
returns: The rule in list rules that matches the char given as a parameter
"""
def applyRules(char, rules):
    for i in rules:
        newList = i.split(':')
        if newList[0] == char:
            return newList[1]
    return char

"""
Processes the axiom and returns the new string
param list: (string) axiom, (list) rules
returns: newString
"""
def processString(axiom, rules):
    newString = ''
    for a in axiom:
        newString += applyRules(a, rules)
    return newString

"""
Creates an L System up to a given number of iterations
params: (int) iterations, (string) axiom, (list) rules
rreturns: axiom with rules applied
"""
def createLSystem(iterations, axiom, rules):
    for i in range(iterations):
        axiom = processString(axiom, rules)
    return axiom

"""
Draws LSystem
params: (string) orders, (int) distance, (int) degree
returns: none
"""
def drawLSystem(orders, distance, degree):
    choco = turtle.Turtle()
    wn = turtle.Screen()
    for x in orders:
        """
        rand_val = random.random()
        if rand_val >= 0.5:
            choco.color("blue")
            choco.pensize(choco.pensize() + 0.5)
        elif rand_val < 0.5:
            choco.color("red")
            if choco.pensize() >= 3:
                choco.pensize(choco.pensize() - 2)
        #if choco.distance(0,0) >= 60:
            #choco.pensize((choco.distance(0,0))/59)
        """
        if x == 'F':
            choco.forward(distance)
        elif x == '+':
            choco.left(degree)
        elif x == '-':
            choco.right(degree)
    wn.exitonclick()



