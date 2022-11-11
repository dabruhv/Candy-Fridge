import random

print("Mild")



candy = [0,0,0,0,0,0]

def rando():
    candy[5] += 1
    for i in range(4):
        egg = random.randrange(0,100)
        if egg <= 15:
            candy[0] += 1
        elif egg <=35:
            candy[1] += 1
        elif egg <= 70:
            candy[2] += 1
        elif egg <= 80:
            candy[3] += 1
        elif egg <= 98:
            candy[4] += 1
        
            

for l in range(5):  
    rando()

print("I got ",candy[0]," butterfingers!")
print("I got ",candy[1]," Hershey's!")
print("I got ",candy[2]," PB cups!")
print("I got ",candy[3]," M&M's!")
print("I got ",candy[4]," Sour Patch Kids!")
print("I got a rock.")
print()
print("Medium")
class fridge:
    def __init__(self):
        
        self.item = 0
        self.isOpen = False
        self.running = True
    
    def info(self):
        print("You have ",self.item," items.")
        if self.isOpen is True:
            print("The door is open.")
        else:
            print("The door is not open.")
        print("Your refridgerator is running go catch it.")
    
    def DoorOpen(self):
        self.isOpen = True
    
    def DoorClose(self):
        self.isOpen = False
        
    def fill(self,num):
        if self.isOpen is True:
            self.item += num
        else:
            print("If only you had magic powers to go through the door...")
            
    def DinDin(self):
        if self.item >= 10:
            self.item -=10
            print("Yummy")
        else:
            print("You're too poor I'm sorry:(")
        
doExit = False  
cold = fridge()

while doExit is False:
    cold.info()
    select = input("You can: (o)pen the door, (c)lose the door, (a)dd food, (d)indin time, or (q)uit")
    if select == 'o':
        cold.DoorOpen()
    elif select == 'c':
        cold.DoorClose()
    elif select == 'a':
        cold.fill(random.randrange(10,30))
    elif select == 'd':
        cold.DinDin()
    elif select == 'q':
        doExit = True
    else:
        print("bruh")
