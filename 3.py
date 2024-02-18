a = 5
b = 14
my_name = "Yoni"
if my_name == "Yoni" and (b >= 10 or a < 50):
    print("You are Yoni")
    print("World")
    print("dude")
elif my_name == "Yoni":
    print("Found your name")
elif b > 5:
    print("b is good")
else:
    print("Crap")

my_list = [2]
if len(my_list):
    print("you have itemsssssss")
else:
    print("no items in the list")

my_other_list = ["or", "yoni", "sdfdsf"]
my_other_name = "or"
if my_other_name in my_other_list:
    print("I found you")
else: print("Continue to search")

tt = [50, 2, 3]
rr = [50, 2, 3]
print(type(tt) is list)
