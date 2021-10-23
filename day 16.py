# import turtle
#
# squirtle = turtle.Turtle()
# print(squirtle)
# squirtle.forward(100)
# turtle.distance(squirtle)
# squirtle.shape("turtle")
# squirtle.color("blue1")
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

# table.field_names = ["Pokemon Names", "Pokemon Type"]
# table.add_row(["Pikachu", "Lightening"])
# table.add_row(["Gengar", "Ghost"])

# Lecturers method


table.add_column("Pokemon Name", ["Pikachu", "Gengar", "Charmander"])
table.add_column("Type", ["Electric", "Ghost", "Fire"])

table.align["Pokemon Name"] = "c"
table.align["Type"] = "c"

print(table)