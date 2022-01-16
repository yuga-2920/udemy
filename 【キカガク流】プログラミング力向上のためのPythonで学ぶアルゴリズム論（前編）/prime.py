import time

def get_prime(max_num):
    
    prime = []

    for i in range( 2, max_num):
        flag = True
        for t in prime:
            if i % t == 0:
                flag = False
                break
        if flag:
            prime.append(i)

    return print(prime)

prime = get_prime(500)