# from turtle import Screen, Turtle
from prettytable import PrettyTable

# timy = Turtle()
#
# print(timy)
# timy.shape("turtle")
# timy.color("#0099FF")
#
# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)

pokemons_table = PrettyTable()

pokemons_table.add_column("Pokemon", ["Pikachu", "Charmander", "Bulbasaur"], 'l')
pokemons_table.add_column("Type", ["Electric", "Fire", "Water"])
pokemons_table.align = 'l'
print(pokemons_table)
