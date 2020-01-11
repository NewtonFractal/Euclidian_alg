import math

solutions = []
solutions_2 = []

def euclidian_alg(number_1, number_2, number_3):
    while True:
        if number_1 % number_2 != 0:
            solutions.extend([number_1, number_2])
        print(number_1, "=", number_2, "*", math.floor(number_1 / number_2), "+", number_1 % number_2)
        number_1, number_2 = number_2, (number_1 % number_2)
        if number_2 == 0:
            print(number_1)
            break
    for x in range(0,int(len(solutions)/2)):
        a,b,c = solutions[-2-(x*2)]%solutions[-1-(x*2)],solutions[-2-(x*2)],solutions[-1-(x*2)]
        print(a,b,c)
euclidian_alg(321,291,6)
