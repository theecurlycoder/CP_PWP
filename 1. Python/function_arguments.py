import turtle

meg_turtle = turtle.Turtle()

# Draw a square
# Function Definition

def draw_square(length, angle):
    meg_turtle.forward(length)
    meg_turtle.right(angle)

    meg_turtle.forward(length)
    meg_turtle.right(angle)

    meg_turtle.forward(length)
    meg_turtle.right(angle)

    meg_turtle.forward(length)
    meg_turtle.right(angle)


draw_square(150,90)
draw_square(65*2,90)
draw_square(95,90)


