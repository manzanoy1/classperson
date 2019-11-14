#Yanira Manzano
#13/11/2019

from Person_Thing import Person

name = "Mimi"

height = "Five foot six"

weight = int("225")

hair_color = "Brown"

my_person = Person(name, height, weight, hair_color)
my_person.description()
my_person.change_hair_color("Hazel")
my_person.weight_update(25)
my_person.description()
