import math
from functools import reduce
import numbers
import numpy as np
from functools import lru_cache
from tqdm import tqdm
from src.utils import fibonacci, get_primes_up_to, get_prime_factors, is_palindrome, sum_to_nb, get_n_primes


def problem_1():
    MAX_NB = 1000
    multiples = [3, 5]

    a = np.arange(start=0, stop=MAX_NB)

    mask = np.zeros_like(a)
    for multiple in multiples:
        mask = np.logical_or(mask, (a % multiple) == 0)
    
    a_multiples = a[mask]
    solution = np.sum(a_multiples)
    
    return solution


def problem_2():
    max_value = 4e6
    f_sum = 0

    f = fibonacci(0)

    step = 0
    while f < max_value:
        if f % 2 == 0:
            f_sum += f
        step += 1
        f = fibonacci(step)
    
    return f_sum


def problem_3(number=600851475143):
    factors = get_prime_factors(number)
    print(f"{factors = }")
    solution = list(factors.keys())[-1]
    return solution


def problem_4(max_number=(999*999)):
    min_nb = 100
    max_nb = 1000
    last = -1
    for i in range(min_nb, max_nb):
        for ii in range(min_nb, max_nb):
            nb = i * ii
            if is_palindrome(nb):
                if nb > last:
                    last = nb
    return last


def problem_5(nb:int=12):
    primes = get_primes_up_to(nb + 1, verbose=False)
    factors = {}
    for i in range(1, nb + 1):
        n_factors = get_prime_factors(i, primes_list=primes)
        for n_k, n_v in n_factors.items():
            v = factors.get(n_k, -1)
            if v < n_v:
                factors[n_k] = n_v
    compose_list = [p ** e for p, e in factors.items()]
    solution = reduce((lambda x, y: x * y), compose_list)
    return solution


def problem_6(nb = 100):
    sum_of_squares = sum([i ** 2 for i in range(nb + 1)])
    square_of_sum = sum_to_nb(nb) ** 2
    solution = square_of_sum - sum_of_squares
    return solution


def problem_7(nb: int = 10_001):
    return get_n_primes(nb)[-1]

def problem_8():
    big_digit = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    d = {
        "idx": -1,
        "sum": -1,
        "lst": []
    }
    max_prd = 0
    window = 13
    for i in range(len(big_digit) - window):
        i_lst = [int(i) for i in big_digit[i:i + window]]
        i_prd = reduce((lambda x, y: x * y), i_lst)
        if i_prd > max_prd:
            max_prd = i_prd
    return max_prd

def problem_9():
    a = 0
    b = 0
    c = 0
    while a < 1000:
        b = a + 1
        while b < 1000:
            c_2 = (a ** 2) + (b ** 2)
            c = c_2 ** (1/2)
            if int(c) == c and b < c:
                if a + b + c == 1000:
                    print(f"{a = } {b = } {c = }")
                    return a * b * c
            if a + b + c >= 1000:
                break
            b += 1
        a += 1

def problem_10(below=int(2e6)):
    primes = get_primes_up_to(below)
    solution = sum(primes)
    return solution

def problem_11():
    grid = [
        [ 8,  2, 22, 97, 38, 15, 00, 40, 00, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62, 00],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65],
        [52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23,  9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92],
        [16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 00, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40],
        [ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54],
        [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48],
    ]
    top = 0
    for i in range(20):
        for j in range(20):
            hor = 1
            ver = 1
            di1 = 1
            di2 = 1
            for w in range(4):
                if j + 4 <= 20:
                    hor *= grid[i][j + w]
                if i + 4 <= 20:
                    ver *= grid[i + w][j]
                if i + 4 <= 20 and j + 4 <= 20:
                    di1 *= grid[i + w][j + w]
                if i + 4 <= 20 and j - 4 >= 0:
                    di2 *= grid[i + w][j - w]
            if top < di1:
                top = di1
            if top < di2:
                top = di2
            if top < ver:
                top = ver
            if top < hor:
                top = hor
    return top


def nb_divisors(nb):
    divisors = 0
    for i in range(1, nb + 1):
        if (nb % i) == 0:
            divisors += 1
    return divisors




def problem_12():
    # primes = get_primes_up_to(int(1e6), verbose=True)
    max_factors = 500
    max_div = 0
    verbose = True
    with tqdm(total=max_factors, disable=not verbose) as pbar:
        i = 5984
        while True:
            triangle_nb = sum_to_nb(i)
            # factors = get_prime_factors(triangle_nb, primes_list=primes)
            divisiors = nb_divisors(triangle_nb)
            # print(f"{i} - {triangle_nb}: {divisiors}")
            if divisiors > max_div:
                pbar.update(divisiors - max_div)
                tqdm.write(f"{i} | {triangle_nb} -> # {divisiors}")
                max_div = divisiors
            if max_div > max_factors:
                break
            i += 1
    return i

def problem_13():
    from src.numbers.problem_13 import _100_numbers_of_50_digits
    result = 0
    for nb in _100_numbers_of_50_digits:
        result += int(nb)
    return str(result)[:10]


def key_with_maxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

def problem_14():
    def collatz(n):
        return (3 * n) + 1 if n % 2 else int(n / 2)
    mem = {
        1: 1
    }
    for seed in tqdm(range(1, int(1e6))):
        s = [seed]
        while True:
            if c := mem.get(s[-1], False):
                size = len(s) + c
                for i, n in enumerate(s):
                    mem[n] = size - i
                break
            s.append(collatz(s[-1]))
    solution = key_with_maxval(mem)
    n = solution
    # print(f" {n} ", end="")
    # while n != 1:
    #     print(f"-{'/' if n % 2 else '*'}->", end="")
    #     n = collatz(n)
    #     print(f" {n} ", end="")
    # print()
    return solution


def problem_15():
    side = 20
    a = side
    b = side
    fct = math.factorial
    solution = fct(a + b) / (fct(a) * fct(b))
    return solution


all_problems = {
    1: problem_1,
    2: problem_2,
    3: problem_3,
    4: problem_4,
    5: problem_5,
    6: problem_6,
    7: problem_7,
    8: problem_8,
    9: problem_9,
    10: problem_10,
    11: problem_11,
    12: problem_12, # nop
    13: problem_13,
    14: problem_14,
    15: problem_15,
}
