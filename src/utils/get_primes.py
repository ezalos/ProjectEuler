from curses.ascii import NL
import math
import fire
from tqdm import tqdm
from time import time


def timer(f):

    def wrapper(*args, **kwargs):
        start = time()
        ret = f(*args, **kwargs)
        end = time()
        print(f'{f.__name__} took {(end-start):.5f} seconds')
        return ret

    return wrapper


@timer
def sieve_of_eratosthenes(n, verbose=False):
    A = [True] * n
    A[0] = False
    # A[1] = False
    sqrt_n = int(n ** (1/2))
    for i in tqdm(range(2, sqrt_n), disable=not verbose):
        if A[i]:
            j = i ** 2
            while j < n:
                A[j] = False
                j += i
    primes = [i for i, a in enumerate(A) if a]
    return primes


@timer
def sieve_of_sundaram(n):
    k = math.floor((n - 1) / 2)
    sqrt_k = int(k ** (1/2))
    A = [True] * (k + 1)
    for i in tqdm(range(1, sqrt_k)):
        j = i
        while (z := i + j + 2 * i * j) <= k:
            A[z] = False
            j += 1
    T = [(2 * i) + 1 for i, a in enumerate(A) if a]
    return [2] + T


@timer
def sieve_of_atkin(limit):
    primes = [2, 3]
    sieve = [False] * (limit + 1)
    x = 1
    xx = x ** 2
    while xx <= limit:
        y = 1
        yy = y ** 2
        while yy <= limit:
            n = (4 * xx) + (yy)
            if n <= limit and n % 12 in [1, 5]:
                sieve[n] ^= True
            n = (3 * xx) + (yy)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True
            n = (3 * xx) - (yy)
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] ^= True
            y += 1
            yy = y ** 2
        x += 1
        xx = x ** 2
    r = 5
    rr = r ** 2
    while rr <= limit:
        if sieve[r]:
            for i in range(rr, limit+1, rr):
                sieve[i] = False
        r += 1
        rr = r ** 2
    
    primes = primes + [i for i, a in enumerate(sieve) if a]
    return primes


def find_primes(n, verbose=False):
    return sieve_of_eratosthenes(n, verbose)

def problem_10(below=int(2e6)):
    primes = sieve_of_eratosthenes(below)
    # primes = sieve_of_sundaram(below)
    # primes = sieve_of_atkin(below)
    solution = sum(primes)
    return solution


if __name__ == "__main__":
    fire.Fire(problem_10)
