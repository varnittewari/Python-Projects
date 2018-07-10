
import turtle as t
import math
import random
from random import randint
import sys


def draw_circle(numberOfRaindrops, area):
    """
A function that creates the number of raindrops depending on the input.
- Creates the circle for the raindrops
- Defines the parameter area
- Creates a random size of the ribbles between the max and min values
- Picks out a random mix of colors for the circle of every raindrop
- Places the raindrops within a random position plcaed within the boundries of the square
- Returns the area of every raindrop created

    """
    if numberOfRaindrops == 0:
        pass
    else:
        t.color("black")
        r = random.randint(1, max_radius())
        area = area + math.pi * r * r
        randomX = random.randint(-boundary() + r * 2, boundary() - r * 2)
        randomY = random.randint(-boundary() + r * 2, boundary() - r * 2)
        randomRipples = random.randint(3, max_ripples())
        randomColor1 = random.random()
        randomColor2 = random.random()
        randomColor3 = random.random()
        t.fillcolor(randomColor1, randomColor2, randomColor3)
        t.begin_fill()
        t.up()
        t.goto(randomX, randomY)
        t.down()
        t.circle(r)
        t.end_fill()
        t.up()
        t.down()
        distance = r

        while randomRipples > 0:

            distance = distance + r
            t.up()
            randomX = randomX - r
            t.goto(randomX, randomY)
            if randomX + distance * 2 < boundary() and randomX > -boundary() and randomY + distance < boundary() and randomY - distance > -boundary():
                t.down()
                t.circle(distance)
                randomRipples = randomRipples - 1
            else:
                break

        draw_circle(numberOfRaindrops - 1, area)

    return (area)


def wrong_number(numberOfRaindrops):
    """
A function to check if the input of number of raindrops is between 1-100
-  If not the it will print a message and the system will exit, otherwise it will just continue
    """

    if numberOfRaindrops > max_raindrops() or numberOfRaindrops < 1:
        print("Pick a number between 1-",max_raindrops())
        sys.exit(0)

    else:
        pass


def max_raindrops():
    """
A function to return the max number of raindrops
    """
    return 100


def max_radius():
    """
A function to return the max number of the radius
    """
    return 20


def max_ripples():
    """
A function to return the max number of ripples
    """
    return 8


def boundary():
    """
A function to return the number of a boundary length
    """
    return 250


def draw_Square():
    """
A function that draws a purple square
    """
    t.down()
    t.color("purple")
    t.fillcolor("purple")
    t.begin_fill()
    t.fd(boundary() * 2)
    t.left(90)
    t.fd(boundary() * 2)
    t.left(90)
    t.fd(boundary() * 2)
    t.left(90)
    t.fd(boundary() * 2)
    t.end_fill()
    t.up


def main(max):
    """
Starts the whole process
- Asks for input of number of raindrops
- Starts the area with value of 0
- Sets the postition of the starting point at -250,-250
- turtle starts up
- Sets turtle speed
- defines areaOfRaindrops
- starts the drawing of the square
- Prints the calculation of the raindrops area

    """

    numberOfRaindrops = int(input("Number of raindrops: "))
    wrong_number(numberOfRaindrops)
    area = 0
    t.up()
    t.setx((-boundary()))
    t.sety((-boundary()))
    t.speed(7)
    draw_Square()
    areaOfRaindrops = draw_circle(numberOfRaindrops, area)
    print("The total area of the raindrops is:" + str(areaOfRaindrops) + " square units")
    t.done()


main(max_raindrops())


#def test_function():
    
    #max_raindrops(0)
    #max_raindrops(4)
    #max_raindrops(105)
