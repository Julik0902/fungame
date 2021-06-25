import turtle
sc=turtle.Screen()
sc.setup(600,600)
spiral=turtle.Turtle()
spiral.speed(5)
sc.bgcolor("black")
col=("yellow","blue","white","green","purple","red","pink","grey","orange")
c=0

for i in range(100):
    spiral.forward(1*i)
    if i % 2 == 0:
        spiral.right(400)
    else:
        spiral.left(200)
    spiral.color(col[c])
    if c==8:
        c=0
    else:
        c+=1