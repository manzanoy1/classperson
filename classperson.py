# Yanira Manzano
#13/11/2019
#Class Person

class Person:
    def __init__(self, name, height, weight, hair_color):
        self.name = name
        self.height = height
        self.weight = weight
        self.hair_color = hair_color

    def description(self):
        print(f"""Hi my name is {self.name}, I'm {self.height} tall. I weight {self.weight}lbs, and I have {self.hair_color} hair.""")

    def change_hair_color(self,new_color):
        self.hair_color = new_color

    def weight_update(self,more_pounds):
        self.weight += more_pounds
