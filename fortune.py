# Problem 6: Fortune
from random import choice
quotes = (open("fortune.txt").read()).split("%")
print(choice(quotes))
