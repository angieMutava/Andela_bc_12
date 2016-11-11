def is_prime(number):
    if number <= 0:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

def prime_generator(number):
    if number < 0:
        return "Negative numbers not allowed."
    if type(number) != int:
        return "Only integers allowed"
    result = []
    for i in range(2, number + 1):
        if is_prime(i):
            result.append(i)
    return result