class snake:
       def move (self):
           print("slithers")
    
class eagle:
         def move (self):
              print("flys")
              
class fish:
        def move (self):
            print("swims")  
            
class kangaroo:
        def move (self):
            print("hops")          
              
animals = [snake(), eagle(), fish(), kangaroo()]
for animal in animals :
    animal.move()