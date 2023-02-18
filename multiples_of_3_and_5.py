# Naomi Tesla
# https://projecteuler.net/problem=1

def multiples_of_3_and_5(n):
    sum = 0
    for i in range (3,n):
        if not i%3:
            sum += i
        elif not i%5:
            sum += i
    return sum


assert multiples_of_3_and_5(1000) == 233168
