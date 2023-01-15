import random
def random_int_multiplier():
    A = random.randint(1, 9)
    B = random.randint(1, 9)
    C = A*B
    while C!= 4:
        print(A)
        print(C)
        A = random.randint(1, 9)
        B = random.randint(1, 9)
        C = A*B
    else:
        print(" Success! A is {} B is {}".format(A, B))
        
random_int_multiplier()
