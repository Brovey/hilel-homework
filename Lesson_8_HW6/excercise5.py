
def gen_primes():  # returns list of ints
    primes = []
    for elements in range(2, 101):
        for i in primes:
            if elements % i == 0:
                break
        else:
            primes.append(elements)
    return (primes)


print(gen_primes())
