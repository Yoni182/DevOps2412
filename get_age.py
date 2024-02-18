class NegativeAgeError:
    pass


def get_user_age():
    try:
        user_age = int(input("Please enter age "))
    except BaseException:
        print("balbla")
    if user_age < 0:
        raise NegativeAgeError("")
    return user_age
