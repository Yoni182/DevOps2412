# # Create a list from 1 to 100 excluding 7 and multiples of 7
# number_list = [num for num in range(1, 101) if num % 7 != 0]
#
# # Print the resulting list
# print(number_list)


# # Create a list from 1 to 100 excluding 7 and multiples of 7
# number_list = [num for num in range(1, 101) if num % 7 != 0]
#
# # Print the resulting list
# print(number_list[:50])
# print(number_list[50:])

def seven_boom():
    # Create a list from 1 to 100
    number_list = list(range(1, 101))

    for num in number_list:
        # Check if the number contains 7 or is divisible by 7
        if '7' in str(num) or num % 7 == 0:
            print("Boom")
        else:
            print(num)


if __name__ == "__main__":
    seven_boom()
