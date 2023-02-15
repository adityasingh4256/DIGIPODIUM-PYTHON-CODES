from turtle import *
speed('fastest')
pencolor('orange')
fillcolor('red')
pensize(2)
dot(10)
side = 4
for i in range(side):
    fd(-50)
    begin_fill()
    for i in range(side):
        fd(-50)
        for i in range(side):
            fd(50/2)
            lt(360/side)
            dot(10)
            circle(-10)
        rt(360/side)
            
    end_fill()
    lt(360/side)
hideturtle()
mainloop()