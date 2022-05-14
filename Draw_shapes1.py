# Manrit Kaur
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


# function for drawing the shapes with the correct location, color, and fill settings

def shape(x, y, shape_color, side_len, fill, side_angle, side_num, pen_size, turtle_vis, turtle_speed):
    carl = turtle.Turtle()
    carl.pensize(pen_size)
    carl.speed(turtle_speed)
    if turtle_vis == 'n':
        carl.ht()
    carl.penup()
    carl.color(shape_color)
    carl.goto(x, y)
    carl.pendown()
    if fill == 'y':
        carl.begin_fill()
        if side_num == 0:
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
        carl.end_fill()
    else:
        if side_num == 0:
            carl.goto(x - side_len, y - side_len)
            carl.circle(side_len)
        elif side_num == 1:
            carl.left(int(turtle.numinput(f'settings for user generated shape {count2} of {num_shapes}',
                                          'Direction for carl to draw the line? '
                                          '(default is right,'
                                          ' input positive angle in degrees to turn carl that many degrees)')))
            carl.forward(side_len)
        else:
            for i in range(side_num):
                carl.forward(side_len)
                carl.left(side_angle)
    carl.ht()


# function for doing what the assignment requires

def assignment():
    # setting up the canvas

    window(400, 400, 'Shapes', 'indigo')

    # drawing a yellow filled hexagon with side lengths of 40

    shape(80, 80, 'yellow', 40, 'y', 60, 6, 1, 'n', 1)

    # drawing a light green filled octagon with side lengths of 30

    shape(-20, 20, 'lightgreen', 30, 'y', 45, 8, 1, 'n', 1)

    # drawing a pink triangle with side lengths of 70

    shape(80, -120, 'pink', 70, 'y', 120, 3, 1, 'n', 1)

    # ending session

    turtle.exitonclick()


# function for drawing user-generated shapes

def user_generated_shape():
    # user inputs number of shapes

    num_shapes = int(input('number of user-generated shapes?\n'))

    # user sets canvas settings

    print('settings for canvas:')
    window(int(input('width of canvas? (pixels)\n')),
           int(input('height of canvas? (pixels)\n')),
           str(input('name of canvas?\n')),
           str(input('background color? '
                     '(name of color no spaces, see https://i.stack.imgur.com/nCk6u.jpg for list of valid colors)\n')))

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
                                           'number of sides? (must be between 3 and 210, or 1 to draw a straight line,'
                                           ' 0 to draw a circle)\n'))

            if (3 > side_num or side_num > 210) and (side_num != 0 and side_num != 1):
                turtle.textinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                 'num sides must be 1, 0, or between 3 and 210, please press enter to try again')

            # running shape function with circle related prompts

            elif side_num == 0:
                shape(int(turtle.numinput(f'settings for user-generated circle {count2} of {num_shapes}',
                                          'x-coordinate for shape to start?(center of circle)\n')),
                      int(turtle.numinput(f'settings for user-generated circle {count2} of {num_shapes}',
                                          'y-coordinate for shape to start?(center of circle)\n')),
                      str(turtle.textinput(f'settings for user-generated circle {count2} of {num_shapes}',
                                           'color? '
                                           '(name of color no spaces,'
                                           ' see https://i.stack.imgur.com/nCk6u.jpg for list of valid colors)\n')),
                      int(turtle.numinput(f'settings for user-generated circle {count2} of {num_shapes}',
                                          'Circle radius? (pixels)\n')),
                      str(turtle.textinput(f'settings for user-generated circle {count2} of {num_shapes}',
                                           'fill? (y/n)\n')),
                      0, side_num, pen_size, turtle_vis, turtle_speed)

                # updating counters for while loops and conditional statements

                count = 0
                count2 += 1
                count3 += 1

            # running shape function with line related prompts

            elif side_num == 1:
                shape(int(turtle.numinput(f'settings for user-generated line {count2} of {num_shapes}',
                                          'x-coordinate for shape to start line?')),
                      int(turtle.numinput(f'settings for user-generated line {count2} of {num_shapes}',
                                          'y-coordinate for shape to start line?')),
                      str(turtle.textinput(f'settings for user-generated line {count2} of {num_shapes}',
                                           'color? '
                                           '(name of color no spaces,'
                                           ' see https://i.stack.imgur.com/nCk6u.jpg for list of valid colors)\n')),
                      int(turtle.numinput(f'settings for user-generated line {count2} of {num_shapes}',
                                          'length of line? (pixels)\n')),
                      str(turtle.textinput(f'settings for user-generated line {count2} of {num_shapes}',
                                           'fill? (y/n)\n')),
                      0, side_num, pen_size, turtle_vis, turtle_speed)

                # updating counters for while loops and conditional statements

                count = 0
                count2 += 1
                count3 += 1

            # running shapes with general prompts

            else:
                shape(int(turtle.numinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                          'x-coordinate for shape to start?(bottom left vertex of shape)')),
                      int(turtle.numinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                          'y-coordinate for shape to start?(bottom left vertex of shape)')),
                      str(turtle.textinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                           'color? '
                                           '(name of color no spaces,'
                                           ' see https://i.stack.imgur.com/nCk6u.jpg for list of valid colors)\n')),
                      int(turtle.numinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                          'length of sides? (pixels)\n')),
                      str(turtle.textinput(f'settings for user-generated shape {count2} of {num_shapes}',
                                           'fill? (y/n)\n')),
                      360 / side_num, side_num, pen_size, turtle_vis, turtle_speed)

                # updating counters for while loops and conditional statements

                count = 0
                count2 += 1
                count3 += 1

    # prompting user to return to program in pycharm to end the program and ending program

    turtle.textinput('System Prompt', 'return to pycharm to end program, press enter to clear prompt')
    turtle.exitonclick()
    finished = str(input('Press y followed by enter when you are ready to end the program\n'))
    if finished == 'y':
        quit()

