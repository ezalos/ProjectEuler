from tqdm import tqdm
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int):
	if n == 0:
		return 1
	if n == 1:
		return 2
	return fibonacci(n - 1) + fibonacci(n - 2)

def get_primes(max_prime=4e6, verbose=True):
	with tqdm(total=max_prime, disable=not verbose) as pbar:
		primes_list = [2]
		for i in range(primes_list[-1] + 1, max_prime):
			is_prime = True
			for prime in primes_list:
				if i % prime == 0:
					is_prime = False
					break
			if is_prime:
				primes_list.append(i)
				pbar.update(primes_list[-1] - primes_list[-2])
		return(primes_list)


def get_prime_factors(number, primes_list=None):
	if number < 2:
		return {}
	if primes_list == None:
		primes_list = [2]
	factors = {}
	nb_primed = number
	for i in range(2, primes_list[-1] + 1):
		if (nb_primed % i) == 0:
			factors[i] = 0
		while (nb_primed % i) == 0:
			nb_primed /= i
			factors[i] += 1

	limit = int(number ** (1/2))
	for i in range(primes_list[-1] + 1, limit):
		is_prime = True
		for prime in primes_list:
			if i % prime == 0:
				is_prime = False
				break
		if is_prime:
			primes_list.append(i)
			if (nb_primed % i) == 0:
				factors[i] = 0
			while (nb_primed % i) == 0:
				nb_primed /= i
				factors[i] += 1
		if i > nb_primed:
			break
	return factors


def is_palindrome(number: int):
	string_number = str(number)
	size = len(string_number)
	half = size // 2
	left = string_number[:half]
	right = string_number[half + (size % 2):]
	return left == right[::-1]
