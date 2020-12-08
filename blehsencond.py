print ('watch the circles be funky woooo!')
from random import*
from time import*
from graphics import*
from math import sqrt

def circle_dis (cir1, cir2):
    center1 = cir1.getCenter()
    center2 = cir2.getCenter()
    
    x1 = center1.getX()
    y1 = center1.getY()
    
    x2 = center2.getX()
    y2 = center2.getY()
    
    dist = sqrt( (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    return dist

def wall_dis (cir1):
    center1 = cir1.getCenter()
    
    x1 = center1.getX()
    y1 = center1.getY()
    
    left = (x1 == 75)
    right = (x1 == 1425)
    top = (y1 == 75)
    bottom =(y1 == 925)

    return left or right or top or bottom
    
    


win = GraphWin("circle funk :D", 1500, 1000)

cir1 = Circle(Point(200,200),   75)
cir2 = Circle(Point(800,300),   75)
cir3 = Circle(Point(500,700),   75)

cir1.setFill("pink")
cir2.setFill("yellow")
cir3.setFill("green")

cir1.draw(win)
cir2.draw(win)
cir3.draw(win)


space = win.checkKey()

x1 = 0.5
x2 = -0.1
x3 = 0.5
y1 = 0.1
y2 = 0.5
y3 = 0.5


while space == "":
    cir1.move(x1,y1)
    cir2.move(x2,y2)
    cir3.move(x3,y3)

    if circle_dis(cir1, cir2) < 150 :
        x1= -x1
        y1= -y1
        x2= -x2
        y2= -y2
    if circle_dis(cir1, cir3) < 150 :
        x1= -x1
        y1= -y1
        x3= -x3
        y3= -y3
    if circle_dis(cir3, cir2) < 150 :  
        x3= -x3
        y3= -y3
        x2= -x2
        y2= -y2
    if wall_dis(cir1):
        x1= -x1
        y1= -y1
    if wall_dis(cir2):
        x2= -x2
        y2= -y2
    if wall_dis(cir3):
        x3= -x3
        y3= -y3
        print ("hitwall")
