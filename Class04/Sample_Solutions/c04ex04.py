"""
Author:         Tim Smith
Description:    Sample solution for Class04 Ex04 (create a monogram drawing function, and demonstrate its usage)
"""

import turtle


def draw_monogram(pen):
    """
    Accepts a turtle object. Prints a monogram starting with the current x, y, and direction setting. Returns
    with the turtle moved back to its original position and direction.
    :param pen:
    :return: void
    """

    ## save the original state of the pen (x, y, and heading) so that we can return to it when done
    start_x = pen.xcor()
    start_y = pen.ycor()
    start_heading = pen.heading()

    # we'll always make sure the pen is down before starting to draw
    pen.pendown()

    # draw a T
    pen.left(90)  # point up
    pen.forward(100)
    pen.left(90)  # turn to the right
    pen.forward(50)
    pen.left(180)  # turn around
    pen.forward(100)

    # move to the next letter
    pen.up()
    pen.forward(150)

    # draw a C
    pen.left(180)
    pen.down()
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)

    # move to the next letter
    pen.up()
    pen.forward(50)

    # draw an S
    pen.down()
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(100)

    # return the turtle to its original state before the function call, and lift pen up.
    pen.penup()
    pen.setx(start_x)
    pen.sety(start_y)
    pen.setheading(start_heading)

    return


def main():
    """
    Main method for program. Prints a monogram 18 times, with each time rotates by 20 degrees.
    :return: void
    """

    # NOTE: For demonstration purposes, I've added a few other neat features to this... such as
    # rotating through a list of colors for each printing of the monogram - and setting the
    # background color and size of the line that turtle will draw (see turtle.pensize()).

    # Initial the screen and instantiate a turtle called marker
    sandbox = turtle.Screen()
    sandbox.bgcolor('black')
    marker = turtle.Turtle()
    marker.pensize(10)
    marker.speed(100)

    # create a list of colors to be used to draw monogram
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    # we want to draw the monogram 18 times
    for i in range(18):
        # rotate through each of the six colors
        marker.pencolor(colors[i % 6])
        # use our function to draw the monogram
        draw_monogram(marker)
        # rotate the turtle left by 20 degrees (since 360//20 is 18, we print the monogram in a full circular pattern)
        marker.left(20)
        marker.forward(10)

    marker.hideturtle()     # before we finish, hide the turtle. It produces a nicer result.

    sandbox.mainloop()


# This only runs the main method if the program is called directly. Otherwise, if attempted to be loaded as a module
# by another python program, it will not run and display "ERROR: Not designed to be imported"
if __name__ == "__main__":
    main()
else:
    print("ERROR: Not designed to be imported")