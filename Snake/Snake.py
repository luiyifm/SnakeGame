import turtle
import time
import random

retraso=0.15
n=0.5
score=0
score_max=0

wn= turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.screensize(650,650)
wn.tracer(n)
wn.setworldcoordinates(-325,-325, 325, 325)

snake=turtle.Turtle(shape="square")
snake.color("green")
snake.direction="stop"
snake.speed(n)
snake.penup()
snake.goto(0,0)

comida = turtle.Turtle(shape="circle")
comida.hideturtle()
comida.color('red')
comida.penup()
comida.goto(random.randint(-300,300),random.randint(-300,300))
comida.showturtle()
comida.speed(0)

marcador=turtle.Turtle()
marcador.hideturtle()
marcador.penup()
marcador.color("white")
marcador.goto(-320,-320)
marcador.write("Score:0 \nBest Score:0")

lose=turtle.Turtle()
lose.hideturtle()
lose.penup()
lose.color("#FF4D2E")

puntaje=turtle.Turtle()
puntaje.hideturtle()
puntaje.penup()
puntaje.color("#FFFFFF")
puntaje.sety(-10)


body=[]

def arriba():
    snake.direction='up'
def abajo():
    snake.direction='down'
def derecha():
    snake.direction='right'
def izquierda():
    snake.direction='left'

def movimiento():
    if snake.direction == 'up':
        y=snake.ycor()
        snake.sety(y+20)
        time.sleep(retraso)
    if snake.direction == 'down':
        y=snake.ycor()
        snake.sety(y-20)
        time.sleep(retraso)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x-20)
        time.sleep(retraso)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x+20)
        time.sleep(retraso)
        

wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')
game_over=False

while True:
    wn.update()

    if snake.distance(comida)<20:
        x = random.randrange(-300, 301, 20)
        y = random.randrange(-300, 301, 20)
        comida.goto(x,y)
        n+=0.5
        snake.speed(n)
        wn.tracer(n)
        retraso-=0.001
        new_body = turtle.Turtle(shape="square")
        new_body.hideturtle()
        new_body.color('green')
        new_body.penup()
        new_body.speed(0)
        new_body.goto(0,0)
        body.append(new_body)

        score+=10
        if score>score_max:
            score_max=score
            marcador.clear()
            marcador.write("Score:{}\nBest Score:{}".format(score,score_max))

    total=len(body)
    for index in range(total-1, 0, -1):
        x= body[index-1].xcor()
        y= body[index-1].ycor()
        body[index].goto(x,y)
        body[index].showturtle()
    
    if total>0:
        x= snake.xcor()
        y= snake.ycor()
        body[0].goto(x,y)
        body[0].showturtle()

    if snake.xcor() >330 or snake.xcor()< -330 or snake.ycor() > 330 or snake.ycor()< -330:
        game_over=True

    if game_over==True:
        lose_score=score
        retraso=0.15
        n=0.5
        for i in body:
            i.clear()
            i.hideturtle()
        snake.hideturtle()
        snake.home()
        snake.showturtle()
        snake.direction='stop'
        body.clear()
        marcador.clear()
        lose.write("GAME OVER", align="center", font=("Press Start 2P",32,"bold"))
        puntaje.write("Score:{}\t\t\tBest Score:{}".format(lose_score,score_max),align="center", font=("Press Start 2P", 10, 'normal'))
        score=0
        game_over=False
        

    if snake.direction != 'stop':
        lose.clear()
        puntaje.clear()
        marcador.write("Score:{}\nBest Score:{}".format(score,score_max))
        game_over= False

    movimiento()

    for i in body:
        if i.distance(snake) < 20:
            game_over=True
            for i in body:
                i.clear()
                i.hideturtle()
            snake.home()
            body.clear()
            snake.direction = "stop"
            
    time.sleep(retraso)



turtle.done()