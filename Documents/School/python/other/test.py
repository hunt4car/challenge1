from graphics import*

def main():
    #window
    win = GraphWin("Hello World",600,600)

    #circle
    center = Point(100,100)
    circ = Circle(center,30)
    circ.setFill("blue")
    circ.draw(win)
    lable = Text(center,"Hello")
    lable.draw(win)

    #square/rectangle
    rect = Rectangle(Point(30,30),Point(70,70))
    rect.setFill("red")
    rect.draw(win)

    #line
    line = Line(Point(0,0),Point(100,100))
    line.draw(win)

    #print center point
    print(center.getX())
    #x represents the point on the X axis on the "center" object that was made for the circe object
    print(center.getY()) #this prints y! :)

    
    
main()
