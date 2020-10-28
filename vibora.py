from turtle import *
from random import randrange
from freegames import square, vector
import random   # Se hace la inclusión de la librería random

# Juan Angel Mora Moreno | A00517141
# Nombre y matrícula

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Función que cambia la dirección de la serpiente
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# Función que detecta si la cabeza de la serpiente colisiona con los ejes
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Función que ejerce el movimiento de la serpiente y de la comida
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    
    # Uso de la función random para escoger un número al azar
    numero = random.randint(1,5)
    
    if not inside(head) or head in snake:
      if numero == 1:
        square(head.x, head.y, 9, 'white')
        update()
        return
      elif numero == 2:
        square(head.x, head.y, 9, 'black')
        update()
        return
      elif numero == 3:
        square(head.x, head.y, 9, 'green')
        update()
        return
      elif numero == 4:
        square(head.x, head.y, 9, 'purple')
        update()
        return
      elif numero == 5:
        square(head.x, head.y, 9, 'yellow')
        update()
        return

    snake.append(head)
    
    # selecciona las posiciones de la aparición de las comidas
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    
    # Selección de color de la serpiente
    for body in snake:
      if numero == 1:
        square(body.x, body.y, 9, 'black')
      elif numero == 2:
        square(body.x, body.y, 9, 'white')
      elif numero == 3:
        square(body.x, body.y, 9, 'yellow')
      elif numero == 4:
        square(body.x, body.y, 9, 'green')
      elif numero == 5:
        square(body.x, body.y, 9, 'blue')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
