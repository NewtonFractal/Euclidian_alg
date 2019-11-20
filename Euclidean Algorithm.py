import math

def euclidian_alg(number_1, number_2):
    while True:
        print(number_1, "=", number_2, "*", math.floor(number_1 / number_2), "+", number_1 % number_2)
        number_1, number_2 = number_2, (number_1 % number_2)
        if number_2 == 0:
            print(number_1)
            return None

euclidian_alg(23023, 18291)
