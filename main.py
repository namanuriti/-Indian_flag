import turtle
s = turtle.Screen()
i = turtle.Turtle()
S = '#f4c430'
B = '#0000ff'
G = '#2d5a27'
BL = '#000000'
s.title('India Flag')

i.penup()
i.left(90)
i.forward(100)
i.right(90)
i.pendown()

#TOP Rectangle
i.color(S, S)
i.begin_fill()
i.forward(100)
i.right(180)
i.forward(200)
i.right(90)
i.forward(50)
i.right(90)
i.forward(200)
i.right(90)
i.forward(50)
i.end_fill()

i.penup()
i.right(90)
i.forward(125)
i.left(90)
i.forward(25)
i.pendown()

#Chakra
i.color(B)
i.circle(25)
i.left(90)
for _ in range(24):
    i.forward(25)
    i.right(15)
    i.backward(25)


i.penup()
i.right(90)
i.forward(25)
i.left(90)
i.forward(125)
i.right(180)
i.pendown()

#BOTTOM Rectangle
i.color(G, G)

i.begin_fill()
for _ in range(2):
    i.forward(200)
    i.left(90)
    i.forward(50)
    i.left(90)
i.end_fill()

i.penup()
i.right(90)
i.forward(100)
i.left(180)
i.pendown()

#Pole
i.color(BL)
i.begin_fill()
i.forward(350)
i.left(90)
i.forward(2)
i.left(90)
i.forward(350)
i.left(90)
i.end_fill()

i.penup()
i.forward(1000)
s.mainloop()