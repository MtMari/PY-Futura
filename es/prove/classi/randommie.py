#define a class: CAR->brand->(speed, comfort, safety, color_customize, width) -> each attribute goes from 0 to 10, EXCEPT READY which has true or false

class Car:
    def __init__(self, name: str, speed, comfort, safety, color_customize, width, ready: bool):
        self.name               = name
        self.speed              = speed
        self.comfort            = comfort
        self.safety             = safety
        self.color_customize    = color_customize
        self.width              = width
        self.ready              = ready

Aygo    = Car("Aygo", 6, 4, 8, 7, 2, True)
Panda   = Car("Panda", 7, 7, 4, 1, 6, True)
Duster  = Car("Duster", 8, 6, 8, 5, 8, False)
Ci3     = Car("Ci3", 7, 7, 3, 9, 7, False)


if Aygo.comfort < Duster.comfort:
    print("Aygo is less comfortable than Duster")


"""if Aygo.ready == True:
    input("The car is ready, would you like to drive it? Y/N ")
    if input("The car is ready, would you like to drive it? Y/N ") == "N":
        print("Turning off...")
        Aygo.ready = False
        print(Aygo.ready)
    else:
        print("Car is being delivered to your door.")
else: 
    print("The selected car is turned off. Would you like to turn it on?")
    """
