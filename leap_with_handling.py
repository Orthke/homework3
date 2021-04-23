#CS 362 HW 1

def is_leap_year(n):
    if n%4 == 0:
        if n%100!=0:
            if n%400!=0:
                return "{} is a leap year".format(n)
    return "{} is not a leap year".format(n)


def has_errs(raw_input):
    for ch in str(raw_input):
        if ord(ch) < 48 or ord(ch) >57:
            return True
    
    return False

user_input = input("Enter a year: ")

if not has_errs(user_input):
    print(is_leap_year(int(user_input)))
else:
    print("Malformed input...")