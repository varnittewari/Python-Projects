import turtle as t

def initialize():
    """
    initializing the program
    pre conditions: pen is up, facing north, pen color is blue
    post conditions: pen is up, facing north, pen colour is blue
    :return:
    """
    t.setup(600,600)
    t.up()
    t.left(90)
    t.color("blue")



def drawOneBowtie(len):
    """
    for making one bowtie
    :param len:
    :return:
    """
    t.down()
    t.right(60)
    t.fd(len)
    t.right(120)
    t.fd(len)
    t.right(120)
    t.fd(len*2)
    t.left(120)
    t.fd(len)
    t.left(120)
    t.fd(len)
    t.right(30)
    t.up()
    t.fd(len/4)
    t.left(90)
    t.down()
    t.color("red")
    t.begin_fill()
    t.circle(len/4)
    t.end_fill()
    t.left(90)
    t.up()
    t.color("blue")
    t.fd(len/4)
    t.right(90)

def drawBowties(depth,len):
    """
    recursive function
    pre conditions: pen is up, facing north, pen color is blue
    post conditions: pen is up, facing north, pen colour is blue
    :param depth:
    :param len:
    :return:
    """
    if depth==0:
        pass
    else:
        drawOneBowtie(len)
        t.left(60)
        t.fd(len*2)
        t.right(90)
        drawBowties(depth-1,len/3)
        t.right(90)
        t.fd(len*2)
        t.left(60)
        t.fd(len*2)
        t.left(90)
        drawBowties(depth-1,len/3)
        t.left(90)
        t.fd(len*2)
        t.fd(len*2)
        t.right(90)
        drawBowties(depth-1,len/3)
        t.right(90)
        t.fd(len*2)
        t.right(60)
        t.fd(len*2)
        t.left(90)
        drawBowties(depth-1,len/3)
        t.left(90)
        t.fd(len*2)
        t.right(60)


def main():
    """
    to implement the program
    :return:
    """
    depth=int(input(" Enter the depth:"))
    len=int(input("Enter the length:"))
    initialize()
    drawBowties(depth,len)

main()
t.done()




