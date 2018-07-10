"""
Name: Varnit Tewari
Email:vxt6823@rit.edu
This is a program to simulate the play of the game of cards in which we have to make a victory pile with the help of two
discard piles. Victory pile is the deck of cards which has cards of consequent number. We find the average of the number
of consecutive cards in the victory pile and the maximum and minimum number of cards in the victory pile.
"""



from rit_lib import *
from myStack import *
from myQueue import *
from myNode import *
import random

def main():
    """
    Prompt user for input corresponding to the number of cards to use in the deck.
    Calls the necessary functions.
    Prints the average , the maximum and minimum number of cards in the victory pile.
    :return:
    """
    queue = createQueue()
    sum=0
    max=0
    numCards= int(input(" Enter the number of cards used in the deck:"))

    min=queue.size
    numGames= int ( input( " Enter the number of games to play in the simulation"))
    for i in range (numGames):
        vic = createStack()
        dis1 = createStack()
        dis2 = createStack()
        c = 1
        for j in range(numCards):
            enqueue(queue, c)
            c += 1
        for i in range(1, random.randint(1, queue.size)):
            shuffle(queue)
        getFirst(vic,dis1,queue.front.data)
        dequeue(queue)
        while emptyQueue(queue) == False:
            algo(queue,vic,dis1,dis2)
        count=fillVictory(vic,dis1,dis2)
        if count > max:
            max=count
        if count < min:
            min=count
        sum = sum +count
    average= float(sum/numGames)
    print ("The average number of cards on the victory pile ", average)
    print ("The maximum number of cards ever achieved on victory pile ", max)
    print ("The minimum number of cards ever achieved on victory pile ", min)


def shuffle(queue):
    """
    shuffles multiple times
    :param queue:
    :return:
    """
    enqueue(queue, queue.front.data)
    dequeue(queue)

def algo(queue,vic,dis1,dis2):
    """
    main play of the game
    :param queue:
    :param vic:
    :param dis1:
    :param dis2:
    :return:
    """
    for i in range(1,random.randint(1,queue.size)):
        shuffle(queue)

    qtop=queue.front.data

    queue.front = queue.front.next
    queue.size -= 1
    k=2
    itt = True
    if qtop==k-1:
        push (vic,k-1)
        while emptyStack(dis1) != True and emptyStack(dis2) != True and itt == True:
            if not emptyStack(dis1) and top(dis1) == top(vic) + 1:
                push(vic, top(dis1))
            elif not emptyStack(dis2) and top(dis2) == top(vic) + 1:
                push(vic, top(dis2))
            else:
                itt = False
    elif qtop==k and emptyStack(vic)==False:
        push (vic,k)
        k+=1
        while emptyStack(dis1) != True and emptyStack(dis2) != True and itt == True:
            if not emptyStack(dis1) and top(dis1) == top(vic) + 1:
                push(vic, top(dis1))
            elif not emptyStack(dis2) and top(dis2) == top(vic) + 1:
                push(vic, top(dis2))
            else:
                itt = False
    elif emptyStack(dis1) != True and qtop < top(dis1):
        push (dis1,qtop)
    elif emptyStack(dis1) and not emptyStack(dis2) and qtop<top(dis2):
        push (dis2, qtop)
    elif emptyStack(dis1) and not emptyStack(dis2) and qtop>top(dis2):
        push (dis1, qtop)
    elif emptyStack(dis1) and emptyStack(dis2):
        push(dis1, qtop)
    else:
        push (dis2,qtop)

def fillVictory(vic,dis1,dis2):
    """
    fills the victory pile
    :param vic:
    :param dis1:
    :param dis2:
    :return:
    """
    count=1
    itt = True
    while emptyStack(dis1) != True and emptyStack(dis2) != True and itt == True:
        if not emptyStack(dis1) and top(dis1) == top(vic) + 1:
            push(vic, top(dis1))
        elif not emptyStack(dis2) and top(dis2) == top(vic) + 1:
            push(vic, top(dis2))
        else:
            itt = False
        count+=1
    return count

def getFirst(vic,dis1,temp):
    """
    enters the first element
    :param vic:
    :param dis1:
    :param temp:
    :return:
    """
    if temp ==1 :
        push(vic,temp)
    else:
        push (dis1,temp)


main()