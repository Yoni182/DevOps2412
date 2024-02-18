# for i in range(5):
#     print("Hello " + str(i))
#
# for i in range(10):
#     print("You are number " + str(i))
#

def my_printer(prefix, amount_of_times):
    for i in range(amount_of_times):
        print(prefix + " " + str(i))


def mul_five(my_number):

    result = my_number * 5
    return result
the_result = mul_five(10)
print(the_result)


my_printer("Hello", 5)
my_printer("You are number ", 10)
