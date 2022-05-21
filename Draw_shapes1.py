#Manrit Kaur
# 5/2022
# draw shapes using turtle

# importing needed modules
import turtle
from turtle import *


# function for defining how the canvas will look
def window(x_len, y_len, canvas_title, canvas_color):
    wn = turtle.Screen()
    wn.bgcolor(canvas_color)
    wn.screensize(canvwidth=x_len, canvheight=y_len)
    wn.title(canvas_title)


# function for defining carl
def carl(pen_size, turtle_speed, turtle_vis):
    carl = turtle.Turtle()
    carl.pensize(pen_size)
    carl.speed(turtle_speed)
    carl.shape("turtle")
    if turtle_vis == 'n':
        carl.ht()


# function to draw the right shape in the right spot
def draw_shape(x, y, side_len, side_angle, side_num):
    carl = turtle.Turtle()
    carl.pensize(pen_size)
    carl.speed(turtle_speed)
    carl.shape("turtle")

    carl.penup()
    carl.color(shape_color)
    carl.goto(x, y)
    carl.pendown()

    if turtle_vis == 'n':
        carl.ht()

    if side_num == 0:
        carl.goto(x - side_len, y - side_len)
        carl.circle(side_len)

    elif side_num == 1:
        carl.left(int(turtle.numinput(f'settings for user generated shape {count2} of {num_shapes}',
                                      'Direction fo r carl to draw the line? '
                                      '(default is right,'
                                      ' input positive angle in degrees to turn carl that many degrees)')))
        carl.forward(side_len)

    else:
        for i in range(side_num):
            carl.forward(side_len)
            carl.left(side_angle)


# function for establishing carl's settings
def shape(x, y, side_len, fill, side_angle, side_num, pen_size, turtle_speed, turtle_vis, shape_color, canvas_color):
    carl = turtle.Turtle()
    carl.pensize(pen_size)
    carl.speed(turtle_speed)
    carl.shape("turtle")
    if turtle_vis == 'n':
        carl.ht()
    count4 = 1
    while count4 == 1:
        if canvas_color == shape_color:
            color_check = str(turtle.textinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                               'shape color is the same as canvas color, continue? (y/n)'))
            if color_check == 'n':
                shape_color = str(turtle.textinput(f'settings for user-generated {shape_name} {count2} of {num_shapes}',
                                                   'color? '
                                                   '(name of color no spaces, '
                                                   'see https://i.stack.imgur.com/nCk6u.jpg '
                                                   'for list of valid colors)\n'))
            else:
                count4 = 0
        else:
            count4 = 0

    if fill == 'y':
        carl.begin_fill()
        draw_shape(x, y, side_len, side_angle, side_num)
        carl.end_fill()
    else:
        draw_shape(x, y, side_len, side_angle, side_num)
    carl.ht()


# requesting and executing user-generated shapes
# user inputs number of shapes
num_shapes = int(input('number of user-generated shapes?\n'))

# user sets canvas settings
print('settings for canvas:')
canvas_color = str(input('background color? '
                         '(name of color no spaces, '
                         'see https://i.stack.imgur.com/nCk6u.jpg for list of valid colors)\n'))
window(int(input('width of canvas? (pixels)\n')),
       int(input('height of canvas? (pixels)\n')),
       str(input('name of canvas?\n')),
       canvas_color)

# Console prompts user to switch to the turtle window, and input the settings for carl
print('switch to turtle window')
pen_size = int(turtle.numinput('settings for carl',
                               'pen size? (positive integer)\n'))
turtle_vis = str(turtle.textinput('settings for carl',
                                  'see carl while he works? (y/n)\n'))
turtle_speed = int(turtle.numinput('settings for carl',
                                   'how fast should carl work? (positive integer)\n'))

# Establishing variables needed later
count2 = 1
count3 = 1
keep_size = ''

# Drawing the shapes
for i in range(int(num_shapes)):

    # checking user if they want to change their pen size, but only if it isn't the 1st shape drawn
    # because user just set their pen size
    if count3 != 1:
        keep_size = str(turtle.textinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                         'keep the same pensize? (y/n)\n'))

    # while loop to only allow the user to draw a closed shape, a circle, or a line,
    count = 1
    while count == 1:

        # acting on user choice to keep or change pen size
        if keep_size == 'n':
            pen_size = int(turtle.numinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                           'pen size? (positive integer)\n'))

        # requesting number of sides
        side_num = int(turtle.numinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                       'number of sides? '
                                       '(must be a positive integer, 1 to draw a line, 0 to draw a circle)\n'))

        # setting up variables for prompts and side angle
        if side_num == 0:
            shape_name = 'circle'
            shape_len = 'length of circle radius'
            shape_loc = '(center of circle)'
            side_angle = 0

        elif side_num == 1:
            shape_name = 'line'
            shape_len = 'length of line'
            shape_loc = ''
            side_angle = 0

        else:
            shape_name = 'shape'
            shape_len = 'length of sides'
            shape_loc = '(bottom left vertex of shape)'
            side_angle = 360 / side_num

            # preventing inputs that will break the program
        if side_num == 2 or side_num < 0:
            turtle.textinput(f'settings for user-generated shape {count2} of {num_shapes}',
                             'num sides must be a positive integer other than 2, 0 for circle '
                             'please press enter to try again')

            # running shape function with correct prompts
        else:
            shape_color = str(turtle.textinput(f'settings for user-generated {shape_name} {count2} of {num_shapes}',
                                               'color? '
                                               '(name of color no spaces,'
                                               ' see https://i.stack.imgur.com/nCk6u.jpg for list of valid colors)\n'))
            shape(int(turtle.numinput(f'settings for user-generated {shape_name} {count2} of {num_shapes}',
                                      f'x-coordinate for {shape_name} to start? {shape_loc}\n')),
                  int(turtle.numinput(f'settings for user-generated {shape_name} {count2} of {num_shapes}',
                                      f'y-coordinate for {shape_name} to start? {shape_loc}\n')),
                  int(turtle.numinput(f'settings for user-generated {shape_name} {count2} of {num_shapes}',
                                      f'{shape_len}? (pixels)\n')),
                  str(turtle.textinput(f'settings for user-generated {shape_name} {count2} of {num_shapes}',
                                       'fill? (y/n)\n')), side_angle, side_num, pen_size, turtle_speed, turtle_vis,
                  shape_color, canvas_color)

            # updating counters for while loops and conditional statements
            count = 0
            count2 += 1
            count3 += 1

# ending session
turtle.exitonclick()
