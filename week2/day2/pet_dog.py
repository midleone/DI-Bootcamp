from random import choice
from dog_classes import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        bark_result = super().bark()
        self.trained = True
        print(bark_result)
        print(f"{self.name} is now trained!")

    def play(self, *dog_names):
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            trick_result = choice(tricks)
            print(trick_result)
        else:
            print(f"{self.name} is not trained yet. Train the dog first.")

pet_dog = PetDog(name="Max", age=2, weight=12)

pet_dog.train()
pet_dog.play("Buddy", "Rocky")
pet_dog.do_a_trick()