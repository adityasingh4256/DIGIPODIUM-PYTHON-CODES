from turtle import*
def polygon(side, dis):
    for i in range(side):
        fd(dis)
        lt(360/side)
bgcolor('red')
pencolor('yellow')
for i in range(3,9):
    polygon(i, i+7)
mainloop()