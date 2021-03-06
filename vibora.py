from turtle import *
from random import randrange
from freegames import square, vector
import random   # Se hace la inclusión de la librería random

# Juan Angel Mora Moreno | A00517141
# Isaac Arredondo Padrón | A00828359

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Función que cambia la dirección de la serpiente
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
    
# Fucion que cambia la dirección de la comida 
def changeFood(x, y):
    food.x += x
    food.y += y
    
# Función que detecta si la cabeza de la serpiente colisiona con los ejes
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Función que ejerce el movimiento de la serpiente y de la comida
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    
    # Los siguientes condicionales hacen que la comida se mueva random y valida que no salga del tablero
    dire = randrange(0,4)
    if (dire == 0 and food.x < 170):
      changeFood(10, 0)
    elif (dire == 1 and food.x > -180):
      changeFood(-10, 0)
    elif (dire == 2 and food.y < 170):
      changeFood(0, 10)
    elif (dire == 3 and food.y > -180):
      changeFood(0, -10)
    
    # Uso de la función random para escoger un número al azar
    numero = random.randint(1,5)
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
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
        square(body.x, body.y, 9, 'orange')
      elif numero == 3:
        square(body.x, body.y, 9, 'yellow')
      elif numero == 4:
        square(body.x, body.y, 9, 'green')
      elif numero == 5:
        square(body.x, body.y, 9, 'blue')
    
    # Selección de color aleatorio de la comida
    if numero == 1:
      square(food.x, food.y, 9, 'orange')
    elif numero == 2:
      square(food.x, food.y, 9, 'black')
    elif numero == 3:
      square(food.x, food.y, 9, 'blue')
    elif numero == 4:
      square(food.x, food.y, 9, 'yellow')
    elif numero == 5:
      square(food.x, food.y, 9, 'green')
    
    update()
    ontimer(move, 100)

# Aqui inicializamos el juego y utilizamos la funcion lambda para cambio de direcciones
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
