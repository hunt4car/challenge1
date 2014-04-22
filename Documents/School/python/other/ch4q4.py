from graphics import *
 
def main():
    win = GraphWin("snowman",500,500)

     

    win.setBackground("blue")        
    #ground
    groundC = color_rgb(239,255,254)
    ground = Rectangle(Point(0,250),Point(503,503))
    ground.setFill(groundC)
    ground.draw(win)

     
    #mountain
    mountainC = color_rgb(143,77,63)
    mountain1 = Polygon(Point(250,250),Point(90,60),Point(0,250))
    mountain1.setFill(mountainC)
    mountain1.draw(win)
     
    mountain2 = Polygon(Point(-1,3),Point(3,5),Point(6,3))
    mountain2.setFill(mountainC)
    mountain2.draw(win) 
 
    #snowmanbody
    body = Circle(Point(250,320),55)
    body.setFill('White')
    body.draw(win)
       
    #face
       
    head = Circle(Point(250,250),30)
    head.setFill('White')
    head.draw(win)
     
    eye1 = Circle(Point(240,235),5)
    eye1.setFill('Black')
    eye1.draw(win)
     
    eye2 = Circle(Point(260,235),5)
    eye2.setFill('Black')
    eye2.draw(win)
     
    nose = Oval(Point(245,250),Point(265,255))
    nose.setFill('Black')
    nose.draw(win)

    mouth = Line(Point(245,270),Point(260,270)).draw(win)
     
     
    
main()
