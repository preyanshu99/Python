import turtle
pen = turtle.Pen()
pen.up()
pen.backward(100)
pen.down()
pen.color('red','yellow')
pen.speed(0)
pen.begin_fill()

#for var in range(100):
  #  pen.circle(var)
 #   pen.left(0)
    
for var in range(200):
	pen.circle(var)
	pen.left(30)
	
	
#for var in range(100):
    #pen.circle(var)
   # pen.left(180)


#for var in range(100):
 #   pen.circle(var)
  #  pen.left(270)

pen.end_fill()
turtle.exitonclick()
