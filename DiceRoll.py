from graphics import *
from random import*
def main():
    

    w = GraphWin()
    s1 = Rectangle(Point(70,70), Point(20,20))
    s1.setFill("Blue")
    s1.draw(w)

    s2 = Rectangle(Point(140, 140), Point (90,90))
    s2.setFill("Green")
    s2.draw(w)

    #Display message
    m = Text(Point(60,10), ("Click to roll dice: "))
    m.draw(w)
    #Define die faces
    center = Point(60,60)
    sd1 = Circle(center, 5)
    sd1.setFill("Red")

    center = Point(45,60)
    sd2 = Circle(center, 5)
    sd2.setFill("Red")

    center3 = Point(30,60)
    sd3 = Circle(center3, 5)
    sd3.setFill("Red")

    center4 = Point(30,30)
    sd4 = Circle(center4, 5)
    sd4.setFill("Red")

    center5 = Point(45,30)
    sd5 = Circle(center5, 5)
    sd5.setFill("Red")

    center6 = Point(60,30)
    sd6 = Circle(center6, 5)
    sd6.setFill("Red")

    center7 = Point(130,130)
    sd7 = Circle(center7, 5)
    sd7.setFill("Red")

    center8 = Point(130,115)
    sd8 = Circle(center8, 5)
    sd8.setFill("Red")

    center9 = Point(130,100)
    sd9 = Circle(center9, 5)
    sd9.setFill("Red")

    center10 = Point(100,100)
    sd10 = Circle(center10, 5)
    sd10.setFill("Red")

    center11 = Point(100,115)
    sd11 = Circle(center11, 5)
    sd11.setFill("Red")

    center12 = Point(100,130)
    sd12 = Circle(center12, 5)
    sd12.setFill("Red")


    #Set loops for each die
    #w.getMouse()
    RN = randint(1,6)
    if RN == 1:
        w.getMouse()
        sd1.draw(w)
    elif RN == 2:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
    elif RN == 3:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
        sd3.draw(w)
    elif RN == 4:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
        sd3.draw(w)
        sd4.draw(w)
    elif RN == 5:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
        sd3.draw(w)
        sd4.draw(w)
        sd5.draw(w)
    elif RN == 6:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
        sd3.draw(w)
        sd4.draw(w)
        sd5.draw(w)
        sd6.draw(w)

    #w.getMouse()
    RN2 = randint(1,6)
    if RN2 == 1:
        w.getMouse()
        sd7.draw(w)
    elif RN2 == 2:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
    elif RN2 == 3:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
        sd9.draw(w)
    elif RN2 == 4:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
        sd9.draw(w)
        sd10.draw(w)
    elif RN2 == 5:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
        sd9.draw(w)
        sd10.draw(w)
        sd11.draw(w)
    elif RN2 == 6:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
        sd9.draw(w)
        sd10.draw(w)
        sd11.draw(w)
        sd12.draw(w)
    sum1=RN2 + RN
    print('total sum= '+str(sum1))
    
def out():
        a=input("how many times do you wanna roll the dice\n")
        c=int(a)
        for b in range (0,c):
                main()

                #print(sum1)
                #break

out()
