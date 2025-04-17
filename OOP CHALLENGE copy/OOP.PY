# pet.py

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 10
        self.happiness = 10
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger by 3 but not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness by 1 but not above 10

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy by 5 but not above 10

    def play(self):
        self.energy = max(0, self.energy - 2)  # Decrease energy by 2 but not below 0
        self.happiness = min(10, self.happiness + 2)  # Increase happiness by 2 but not above 10
        self.hunger = min(10, self.hunger + 1)  # Increase hunger by 1 but not above 10

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)  # Increase happiness when learning a new trick

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        

# Create a pet instance
my_pet = Pet("Fluffy")

# Perform some actions
my_pet.get_status()
my_pet.play()
my_pet.get_status()
my_pet.eat()
my_pet.sleep()
my_pet.train("Roll over")
my_pet.train("Fetch")
my_pet.get_status()
my_pet.show_tricks()