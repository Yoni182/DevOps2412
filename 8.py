details = ["Yoni", "Chesla", 36, True]
details_dict = {"fname": "Yoni",
                "lname": "Chesla",
                "age": 36,
                "is_married": True}
my_class = [
    {"fname": "Yossi", "lname": "Asulin"},
    {"fname": "Beber", "lname": "Benishu"}
]
for students in my_class:
    print(students["fname"])

print(details_dict.keys())
print(details_dict.values())