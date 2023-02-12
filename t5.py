from turtle import*
side = 8
for i in range(side):
    pencolor('blue')
    bgcolor('brown')
    circle(10)
    dot(20)
    fd(100)
    lt(360/side)
   
mainloop()