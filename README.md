 ## Snake Game in Python

### Step 1: Import the necessary libraries
```python
import turtle
import time
import random
```

### Step 2: Set up the screen
```python
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.screensize(650, 650)
wn.tracer(0.5)
wn.setworldcoordinates(-325, -325, 325, 325)
```

### Step 3: Create the snake
```python
snake = turtle.Turtle(shape="square")
snake.color("green")
snake.direction = "stop"
snake.speed(0.5)
snake.penup()
snake.goto(0, 0)
```

### Step 4: Create the food
```python
food = turtle.Turtle(shape="circle")
food.hideturtle()
food.color('red')
food.penup()
food.goto(random.randint(-300, 300), random.randint(-300, 300))
food.showturtle()
food.speed(0)
```

### Step 5: Create the scoreboard
```python
score = 0
score_max = 0

marcador = turtle.Turtle()
marcador.hideturtle()
marcador.penup()
marcador.color("white")
marcador.goto(-320, -320)
marcador.write("Score:0 \nBest Score:0")
```

### Step 6: Create the game over screen
```python
lose = turtle.Turtle()
lose.hideturtle()
lose.penup()
lose.color("#FF4D2E")

puntaje = turtle.Turtle()
puntaje.hideturtle()
puntaje.penup()
puntaje.color("#FFFFFF")
puntaje.sety(-10)
```

### Step 7: Define the functions
```python
def arriba():
    snake.direction = 'up'


def abajo():
    snake.direction = 'down'


def derecha():
    snake.direction = 'right'


def izquierda():
    snake.direction = 'left'


def movimiento():
