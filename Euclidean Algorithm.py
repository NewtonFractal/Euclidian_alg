import math

def euclidian_alg(number_1, number_2):
    print(number_1, "=",number_2,"*", math.floor(number_1 / number_2), "+", number_1 % number_2)
    while True:
        number_1, number_2 = number_2, (number_1 % number_2)
        if number_2 == 0:
            print(number_1)
            return None
        else:
            print(number_1, "=",number_2,"*", math.floor(number_1 / number_2), "+", number_1 % number_2)

euclidian_alg(23023, 18291)
