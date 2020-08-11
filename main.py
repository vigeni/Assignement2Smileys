import random
import turtle
guessesTaken = 0

number = random.randint(1, 10)
print('Mundohu te gjesh numrin qe une po mendoj')

def draw_sad():
  neutral = turtle.Turtle()
  neutral.speed(20)
  neutral.penup()
  neutral.fillcolor('yellow')
  neutral.pendown()
  neutral.begin_fill()
  neutral.circle(100)
  neutral.end_fill()
  neutral.penup()

  neutral.fillcolor('black')
  neutral.goto(-40, 120)
  neutral.begin_fill()
  neutral.pendown()
  neutral.circle(10)
  neutral.penup()
  neutral.end_fill()

  neutral.goto(40, 120)
  neutral.begin_fill()
  neutral.pendown()
  neutral.circle(10)
  neutral.penup()
  neutral.end_fill()

  neutral.goto(40, 50)
  neutral.seth(135)
  neutral.pensize(6)
  neutral.pendown()
  neutral.circle(60, 90)
  neutral.penup()

  neutral.ht()


def draw_happy():
  happy = turtle.Turtle()
  happy.speed(8)
  happy.penup()
  happy.fillcolor('yellow')
  happy.pendown()
  happy.begin_fill()
  happy.circle(100)
  happy.end_fill()
  happy.penup()

  happy.fillcolor('black')
  happy.goto(-40, 120)
  happy.begin_fill()
  happy.pendown()
  happy.circle(10)
  happy.penup()
  happy.end_fill()

  happy.goto(40, 120)
  happy.begin_fill()
  happy.pendown()
  happy.circle(10)
  happy.penup()
  happy.end_fill()

  happy.goto(-40, 50)
  happy.seth(-40)
  happy.pensize(6)
  happy.pendown()
  happy.circle(60, 90)
  happy.penup()

  happy.ht()

def draw_neutral():
  neutral = turtle.Turtle()
  neutral.speed(20)
  neutral.penup()
  neutral.fillcolor('yellow')
  neutral.pendown()
  neutral.begin_fill()
  neutral.circle(100)
  neutral.end_fill()
  neutral.penup()

  neutral.fillcolor('black')
  neutral.goto(-40, 120)
  neutral.begin_fill()
  neutral.pendown()
  neutral.circle(10)
  neutral.penup()
  neutral.end_fill()

  neutral.goto(40, 120)
  neutral.begin_fill()
  neutral.pendown()
  neutral.circle(10)
  neutral.penup()
  neutral.end_fill()

  neutral.goto(-30, 50)
  neutral.pensize(6)
  neutral.pendown()
  neutral.forward(60)
  neutral.penup()

  neutral.ht()

while guessesTaken < 5:
  guess = input()
  guess = int(guess)

  guessesTaken = guessesTaken + 1

  if guess == number:
    print('Bravo! Ti e gjete numrin me ' + str(guessesTaken) + ' tentativa!')
    draw_happy()
    guessesTaken = str(guessesTaken)
    break
  
  if abs(guess - number) <= 2:
    draw_neutral()
    print('Shume afer!')

  if abs(guess - number) > 2 and guess < number:
    draw_sad()
    print('Shume ulet.')

  if abs(guess - number) > 2 and guess > number:
    draw_sad()
    print('Shume larte.')



if guess != number:
  number = str(number)
  print('Jo, numri qe une po mendoja eshte ' + number)