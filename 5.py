# my_name = "Yoni"
# print(list(range(2, 8)))
# print("Hello " + my_name)
# print("Hello " + my_name)
# print("Hello " + my_name)
# print("Hello " + my_name)
# print(type(int))

for i in range(5):
    print("hello " + str(i))
else:
    print("Finished")

# class_mates = ["Yoni", "Maksin", "Gilad", "Oren"]
# # for name in class_mates:
# #     print(name)
#
for i in range(len(class_mates)):
    print(class_mates[i])

your_name = input("Please enter your name: ")
while your_name != "Yoni":
    print("You are not Yoni")
    your_name = input("Enter your name: ")
    if your_name == "haim":
        print("wow")
        break
    if your_name == "baba":
        print("Nice")