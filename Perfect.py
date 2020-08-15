# Python 3.7
# This Program takes an input of any number and tells if it is perfect, almost perfect (within 2 of being perfect), or not perfect
# This Program solves the Perfect Number USACO problem
# By Yusuf Ali

def PerfectNumbers(number):
    divisors = []
    for i in range(number+1):
        if i == 0:
            continue
        else:
            if number % i == 0:
                divisors.append(number)
                divisors.append(i)
            else:
                continue

    for num in divisors:
        if num == number:
            divisors.remove(number)
        else:
            continue
    divisors.remove(number)

    sum_of_divisors = sum(divisors)

    if sum_of_divisors == number:
        result = (str(number) + " is a Perfect Number")
        return result

    elif sum_of_divisors + 2 == number or sum_of_divisors + 1 == number or sum_of_divisors - 1  == number or sum_of_divisors - 2 == number:
        result = (str(number)+" is almost a Perfect Number")
        return result
    else:
        result = (str(number) + " is not Perfect")
        return result

print(PerfectNumbers(8128))