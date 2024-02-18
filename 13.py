def add_names_to_file():
    # Prompts the user to input three names and adds them to 'names.txt' file.

    names = []
    print("Please enter three names:")
    for _ in range(3):
        name = input("Enter a name: ")
        names.append(name)

    with open('names.txt', 'a') as file:
        for name in names:
            file.write(name + '\n')


def print_names_from_file():
    # Prints all names from the 'names.txt' file.

    with open('names.txt', 'r') as file:
        for name in file:
            print(name.strip())


print(add_names_to_file())
print(print_names_from_file())
