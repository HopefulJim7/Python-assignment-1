class Mango_Tree: 
    def Mango_Tree (self):                                  
       species = "Mangifera indica"
       age = 25  # in years
       height = 10.5  # in meters
       fruit_color = "goldenyellow"

    print("Mango fruit are the sweetes and juiciest fruits of all fruits.")
        


class fruit:
    def __init__(fruit, name, color, taste):
        fruit.name = name
        fruit.color = color
        fruit.taste = taste

fruit1 = fruit("Mango", "Yellow", "Sweet")
fruit2 = fruit("Lemons", "Green", "Sour")
fruit3 = fruit("Apple", "Red", "Sweet")
fruit4 = fruit("grapefruit", "yellow", "bitter")
fruit5 = fruit("Orange", "Orange", "Sweet")
    
print(fruit1.name)
print(fruit2.color,)
print(fruit3.taste)
print(fruit4.name)
print(fruit5.color)
    
        
        
class SecretStash:
    def __init__(self):
        self.__temperature = 21  # Private attribute

    def take_temperature(self):
        if self.__temperature > 30:
            self.__temperature -= 1
            print("Clothe yourself in lightweight fabrics!")
        elif self.__temperature > 1 - 20:
            self.__temperature -= 1
            print("Dress in loose fitting clothes!")
        else:
            print("Do winter wear!")
            
    def get_temperature(self):
     return self.__temperature

stash = SecretStash()
stash.take_temperature()
stash.get_temperature()
print(stash.get_temperature())  