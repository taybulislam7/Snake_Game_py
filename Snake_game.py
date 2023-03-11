#snake game
import turtle
import time
import random


delay=0.1

#score
score = 0
high_score = 0

#scern setup
win=turtle.Screen()
win.title('SNAKE GAME')
win.bgcolor('thistle')
win.setup(width=600 ,height=600)
win.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('black')
head.penup()
head.goto(0,0)
head.direction='stop'

#sanke food 
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('red')
food.penup()
food.goto(0,100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0 | High Score: 0', align='center', font=('Dungeon', 20, 'bold'))

#function
def go_up():
    if head.direction != 'down':
        head.direction='up'
def go_down():
    if head.direction != 'up':
        head.direction='down'
def go_left():
    if head.direction != 'right':
        head.direction='left'
def go_right():
    if head.direction != 'left':
        head.direction='right'

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)

#keyboard bindings
win.listen()
win.onkeypress(go_up,'w')
win.onkeypress(go_down,'s')
win.onkeypress(go_left,'a')
win.onkeypress(go_right,'d')


#main game loop
while True:
    win.update()

    #check for a collison with the border 
    if head.xcor()>285 or head.xcor()<-285 or head.ycor()>285 or head.ycor()<-285:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
    
    time.sleep(delay)
    if head.distance(food)<20:
        #move food
        food.goto(random.randint(-285,285),random.randint(-285,285))

        #add a segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('tomato')
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.001

        #Increase the score
        score+=1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write('Score: {} | High Score: {}'.format(score, high_score), align='center', font=('Dungeon', 20, 'bold'))

    #move the end segments first in reverese order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()

    #check for head collision with the body segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            #Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            #clear the segments
            segments.clear()
            #Reset the score
            score = 0

            #Reset the delay
            delay = 0.1
            


            #update the score display
            pen.clear()
            pen.write('Score: {} | High Score: {}'.format(score, high_score), align='center', font=('Dungeon', 20, 'bold'))


win.mainloop()