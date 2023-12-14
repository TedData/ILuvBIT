def spiral(num_lines,step_size):
	import turtle
	temp = step_size
	turtle.showturtle()
	while num_lines > 0:
		turtle.forward(temp)
		turtle.left(90)
		turtle.forward(temp)
		turtle.left(90)
		temp += step_size
		num_lines -= 2
	turtle.exitonclick()

spiral(20, 20)