from turtle import*
side = 4
pencolor("blue")
bgcolor('brown')
begin_fill()
fillcolor('red')
for i in range(side):
    
    fd(150)
    lt(360/side)
end_fill()
fillcolor('yellow')
begin_fill()
circle(50)
end_fill()
mainloop()