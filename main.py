from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0,0)
snake = [vector(0,0)]
target = vector(0,10)

def change (x,y):
    target.x = x
    target.y = y

def inside(head):
    return -200 < head.x <190 and -200 < head.y <190

def move():
    head = snake[-1].copy()
    head.move(target)

    if not inside(head) or head in snake:
        square(head.x, head.y, 0, 'red')
        return
    snake.append(head)

    if head == food:
        print('snake:', len(snake))
        food.x = randrange(-15,15)* 10
        food.y = randrange(-15, 15)* 10
    else:
            snake.pop(0)
    clear()
    for body in snake:
        square(body.x, body.y, 9,'black')
    square(food.x, food.y, 9,'green')
    update()
    ontimer(move, 100)

setup(420, 420, 870, 178)
hideturtle()
tracer(False)
listen()
onkey(lambda:change(10, 0), ' Right')
onkey(lambda:change(-10, 0), 'Left')
onkey(lambda:change(0, 18), ' Up')
onkey(lambda:change(0, -18),'Down')
move()
done()

#it was Learning Porpose.
#happy Coding.