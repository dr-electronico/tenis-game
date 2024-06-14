import turtle as t
import os

playerAscore = 0
playerBscore = 0
score_limit = 5

# Create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("The Pong Game")
window.setup(width=800, height=600)
window.tracer(0)

# Register the image of the tennis court
window.addshape("tennis_court.gif")
window.bgpic("tennis_court.gif")

# Creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("red")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("blue")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Code for creating the ball
ball = t.Turtle()
ball.speed(100)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(5, 5)
ballxdirection = 3
ballydirection = 3

# Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=('Arial', 24, 'normal'))

# Code for moving the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    if y < 260:
        y = y + 20
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    if y > -240:
        y = y - 20
    leftpaddle.sety(y)

# Code for moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    if y < 260:
        y = y + 20
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    if y > -240:
        y = y - 20
    rightpaddle.sety(y)

# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

# Function to reset the game
def reset_game():
    global playerAscore, playerBscore
    playerAscore = 0
    playerBscore = 0
    ball.goto(0, 0)
    ballxdirection = 2
    ballydirection = 2
    pen.clear()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=('Arial', 24, 'normal'))

# Function to update the score and check for a winner
def update_score():
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(playerAscore, playerBscore), align="center", font=('Arial', 24, 'normal'))
    if playerAscore >= score_limit:
        pen.goto(0, 0)
        pen.write("Player A Wins!", align="center", font=('Arial', 24, 'normal'))
        return True
    elif playerBscore >= score_limit:
        pen.goto(0, 0)
        pen.write("Player B Wins!", align="center", font=('Arial', 24, 'normal'))
        return True
    return False

while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Border set up
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerAscore = playerAscore + 1
        if update_score():
            response = t.textinput("Game Over", "Player A Wins! Do you want to play again? (yes/no):")
            if response.lower() == 'yes':
                reset_game()
            else:
                break
        os.system("afplay wallhit.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        if update_score():
            response = t.textinput("Game Over", "Player B Wins! Do you want to play again? (yes/no):")
            if response.lower() == 'yes':
                reset_game()
            else:
                break
        os.system("afplay wallhit.wav&")

    # Handling the collisions with paddles
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50):
        ball.setx(340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")
