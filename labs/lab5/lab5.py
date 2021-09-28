# Jacob Ullman
# Lab5
#
from math import sqrt

from graphics import GraphWin, Point, Text, Polygon, color_rgb, Circle, Entry


def triangle():
    # Creates a graphical window
    width = 400
    height = 400
    graphics = GraphWin("Lab 5", width, height)

    # number of times user can create points
    num_clicks = 3

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click 3 times to set the triangle's corners.")
    instructions.draw(graphics)

    # allows the user to click multiple times to set the triangle
    for i in range(num_clicks):
        p1 = graphics.getMouse()
        p2 = graphics.getMouse()
        p3 = graphics.getMouse()
        tri = Polygon(p1, p2, p3)
        tri.setOutline("blue")
        tri.setFill("black")
        tri.draw(graphics)

        dx1 = p1.getX() - p2.getX()
        dx2 = p2.getX() - p3.getX()
        dx3 = p3.getX() - p1.getX()
        dy1 = p1.getY() - p2.getY()
        dy2 = p2.getY() - p3.getY()
        dy3 = p3.getY() - p1.getY()
        l1 = sqrt(dx1 ** 2 + dy1 ** 2)
        l2 = sqrt(dx2 ** 2 + dy2 ** 2)
        l3 = sqrt(dx3 ** 2 + dy3 ** 2)
        perimeter = l1 + l2 + l3
        s = perimeter / 2
        perimeter = str(perimeter)
        display = Text(inst_pt, "The perimeter is " + perimeter)
        instructions.undraw()
        display.draw(graphics)

        area_pt = Point(width / 2, height - 30)
        area = sqrt(s * (s - l1) * (s - l2) * (s - l3))
        area = str(area)
        display2 = Text(area_pt, "The area is " + area)
        display2.draw(graphics)
    graphics.getMouse()
    graphics.close()


def color_shape():
    # Creates a graphical window
    width = 400
    height = 400
    graphics = GraphWin("Lab 5", width, height)

    # number of times user can alter RGB values
    num_rgb = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Enter a number between 0-255 for Red Blue and Green.")
    instructions.draw(graphics)

    # builds a circle
    shape = Circle(Point(200, 100), 100)
    shape.setOutline("black")
    shape.setFill(color_rgb(0, 0, 0))
    shape.draw(graphics)

    r_pt = Point(width / 2, height - 50)
    g_pt = Point(width / 2, height - 70)
    b_pt = Point(width / 2, height - 90)

    rbox = Entry(r_pt, 30)
    gbox = Entry(g_pt, 30)
    bbox = Entry(b_pt, 30)

    rbox.draw(graphics)
    gbox.draw(graphics)
    bbox.draw(graphics)

    # allows the user to set the RGB values 5 times
    for i in range(num_rgb):
        graphics.getMouse()
        r = rbox.getText()
        g = gbox.getText()
        b = bbox.getText()
        r = eval(r)
        g = eval(g)
        b = eval(b)

        shape.setFill(color_rgb(r, g, b))

    graphics.getMouse()
    graphics.close()


def process_string():
    userinput = eval(input("Please enter text: "))
    first = userinput[0]
    print(first)  # first letter
    last = userinput[-1]
    print(last)  # last letter
    twotofive = userinput[2, 6]
    print(twotofive)  # letters in pos 2-5
    firstlast = first + last
    print(firstlast)  # first and last letter
    firstthree = userinput[0, 3]
    firstthree = firstthree + firstthree + firstthree + firstthree + firstthree + firstthree + firstthree + firstthree + firstthree + firstthree
    print(firstthree)  # first three letters
    l = len(userinput)
    for i in range(0, l):
        count = 0
        print(userinput[count])  # each letter printed individually
        count = count + 1
    print(l)  # number of characters


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']
    l = len(values)
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] + values[1] + values[1] + values[1] + values[1]
    print(x)
    x = [values[2], values[3], pt]
    print(x)
    x = [values[2], values[3], 5]
    print(x)
    x = [values[2], values[0], values[-1]]
    print(x)
    x = values[2] + values[0] + values[-1]
    print(x)
    x = l
    print(x)


def another_series():
    userinput = eval(input("Please enter number of terms: "))
    l = userinput
    sumint = 0
    for i in range(0, l):
        count = 1
        sums = [0,l]
        if count == 3:
            sums[i] = 6
            count = 1
            sumint = sumint + sums[i]
        if count == 2:
            sums[i] = 4
            count = 3
            sumint = sumint + sums[i]
        if count == 1:
            sums[i] = 2
            count = 2
            sumint = sumint + sums[i]
        print(sumint)

