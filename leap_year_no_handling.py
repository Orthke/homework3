#CS 362 HW 1

def is_leap_year(n):
    if n%4 == 0:
        if n%100!=0:
            if n%400!=0:
                return "{} is a leap year".format(n)
    return "{} is not a leap year".format(n)


user_input = int(input("Enter a year: "))

print(is_leap_year(user_input))