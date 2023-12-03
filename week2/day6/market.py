class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity

    def get_info(self):
        result = f"{self.name}'s farm\n"
        for animal, quantity in self.animals.items():
            result += f"{animal} : {quantity}\n"
        return result + "E-I-E-I-0!"

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = ', '.join(self.get_animal_types())
        return f"{self.name}'s farm has {animal_types}."


# Example usage:
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
#
print(macdonald.get_short_info())