# shape demo
import turtle
turtle.right(25)
turtle.forward(15)

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600
CHROME_WIDTH = 30  # allow for window borders, title bar, etc.
SHAPE_CHOICES = 3

def circle(bounds):
    turtle.penup()
    center_x = bounds['x'] + bounds['width'] // 2
    bottom_y = bounds['y']
    turtle.setposition(center_x, bottom_y)
    turtle.pendown()

    turtle.circle(min(bounds['width'], bounds['height']) // 2)

def triangle(bounds):
    circle(bounds)

def square(bounds):
    circle(bounds)

def pentagon(bounds):
    circle(bounds)

def hexagon(bounds):
    circle(bounds)

def heptagon(bounds):
    circle(bounds)

DESCRIPTION, FUNCTION = 0, 1

shapes = [("Circle", circle), ("Triangle", triangle), ("Square", square), ("Hexagon", hexagon), ("Heptagon", heptagon)]

choices = []

turtle.setup(CANVAS_WIDTH + CHROME_WIDTH, CANVAS_HEIGHT + CHROME_WIDTH)

for _ in range(SHAPE_CHOICES):

    for i, (description, function) in enumerate(shapes):
            print("{}. {}".format(i + 1, description))

    choice = int(input("Choose one number from the above: ")) - 1

    choices.append(shapes[choice][FUNCTION])

    del shapes[choice]

x, y = -CANVAS_WIDTH // 2, -CANVAS_HEIGHT // 2

width, height = CANVAS_WIDTH // SHAPE_CHOICES, CANVAS_HEIGHT // SHAPE_CHOICES

# I'm dividing the screen into thirds both horizontally and vertically
bounds = dict(x=x, y=y, width=width, height=height)

for choice in choices:
    choice(bounds)

    bounds['x'] += width
    bounds['y'] += height

turtle.done()




wn.exitonclick()
