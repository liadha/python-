from animal import Animal
class Dog(Animal):
    def __init__(self, km):
        super().__init__()
        self.km = km

    def run(self):
        print("dog run km : ", self.km)

    def dog_make_sound(self):
        super().sound("hav hav")

    def move(self):
        print("dog move")



