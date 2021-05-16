import cowsay
import random
import time
# oh god this is edgy...
def again():
    list1 = ["The human race don't deserve rights.", "I fucking wish the human race was dead.", "The Joker was right all along.",  "Dababy isn't a good artist.", "Ever since the human race killed my cow friend, I've always hated them back since."]
    cowsay.cow(random.choice(list1))
    time.sleep(2)
    print("Yeah... I'm sorry.")
again()
x = input("do it another time? (y/anything else) ")
if x == "y":
    again()
else:
    exit()
    
