# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

# years divisible by 4 are leap years
# but years divisible by 100 are not leap years
# but years divisible by 400 are leap years

def is_leap_year(year):
    div400 = 400
    div4= 4
    div100 = 100
    if (year%div4 == 0 and year%div100 != 0):
        return True
    elif(year%div400 == 0 and year%div100 == 0):
        return True
    else:
        return False
    