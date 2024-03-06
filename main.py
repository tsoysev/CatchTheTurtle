import turtle
import random

gameScreen = turtle.Screen()
gameScreen.bgcolor("light yellow")
gameScreen.title("Catch the Turtle")
FONT = ("Arial",30,"normal")
score  = 0
gameOver = False
gridSize = 180


# turtle list
turtleList = []

# score turtle
scoreTurtle = turtle.Turtle()

# countdown tuttle
countdownTurtle = turtle.Turtle()
def setupScoreTurtle():
    scoreTurtle.hideturtle()
    scoreTurtle.color("dark blue")

    scoreTurtle.penup()

    topHeight = gameScreen.window_height() / 2
    y = topHeight * 0.9

    scoreTurtle.setpos(0,y)
    scoreTurtle.write(arg="Score: 0",move=False,align="center",font=FONT)
    


def makeTurtle(x,y):
    t = turtle.Turtle()
    def handleClick(x,y):
        global score
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write(arg=f"Score: {score}",move=False,align="center",font=FONT)
        t.hideturtle()
        t.pos()
        
    
    
    t.onclick(handleClick)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x * gridSize,y * gridSize)
    turtleList.append(t)

def setupTurtles():
    for i in range(-2,3):
        for j in range(-2,2):
            makeTurtle(i,j)
            
def hideTurtles():
    for t in turtleList:
        t.hideturtle()
  
# recursive function      
def showTurtlesRandomly():
    if not gameOver:
        hideTurtles()
        random.choice(turtleList).showturtle()
        if score <= 3:
            gameScreen.ontimer(showTurtlesRandomly,2000)
        elif 7 >= score > 3:
            gameScreen.ontimer(showTurtlesRandomly,1000)
        else:
            gameScreen.ontimer(showTurtlesRandomly,500)            
    else:
        hideTurtles()

def countdown(time):
    global gameOver
    countdownTurtle.hideturtle()
    countdownTurtle.color("dark blue")

    countdownTurtle.penup()

    topHeight = gameScreen.window_height() / 2
    y = topHeight * 0.9

    countdownTurtle.setpos(0,y-40)
    
    
    countdownTurtle.clear()
    if time > 0 and score < 10:
        countdownTurtle.clear()
        countdownTurtle.write(arg=f"Time: {time}",move=False,align="center",font=FONT)
        gameScreen.ontimer(lambda: countdown(time - 1),1000)
        
    elif time > 10 and score == 10:
        gameOver = True
        countdownTurtle.clear()
        hideTurtles()
        countdownTurtle.write(arg="SEN ALLAME-İ CİHANSIN!!!",move=False,align="center",font=FONT)
    elif 10 >= time > 5 and score == 10:
        gameOver = True
        countdownTurtle.clear()
        hideTurtles()
        countdownTurtle.write(arg="Fena değil, idare eder...",move=False,align="center",font=FONT)
    elif 5 >= time > 0 and score == 10:
        gameOver = True
        countdownTurtle.clear()
        hideTurtles()
        countdownTurtle.write(arg="İç güveysinden hallice...",move=False,align="center",font=FONT)
    elif time == 0 and 10 > score >= 6:
        gameOver = True
        countdownTurtle.clear()
        hideTurtles()
        countdownTurtle.write(arg="Üzgünüm, olmadı..",move=False,align="center",font=FONT)
    else:
        gameOver = True
        countdownTurtle.clear()
        hideTurtles()
        countdownTurtle.write(arg="Bayaa bir sıkıntılıymışsın..",move=False,align="center",font=FONT)

def startGameUp():
    turtle.tracer(0)
    setupScoreTurtle()
    setupTurtles()
    hideTurtles()
    showTurtlesRandomly()
    countdown(30)
    turtle.tracer(1)
    
    
startGameUp()

turtle.mainloop()

