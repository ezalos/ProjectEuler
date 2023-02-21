import math

def mean(l):
    return sum(l) / len(l)

def get_chandelier_gravity_center(board):
    epsilon = 1e-10
    xs = []
    ys = []
    n = len(board)
    for i, c in enumerate(board):
        if board[i]:
            theta = (i * 2 * math.pi) / n
            x = math.cos(theta)
            y = math.sin(theta)
            xs.append(x)
            ys.append(y)
    c = sum((abs(mean(xs)), abs(mean(ys))))
    return c


def is_equalized_pair(board):
    half_len = int(len(board) / 2)
    for i, c in enumerate(board):
        if i >= half_len:
            coef = -1
        else:
            coef = 1
        if board[i]:
            if not board[i + (coef * half_len)]:
                return False
    return True


def fill_all_chandeliers_recur(board, index, nb_candles, total_candles):
    if nb_candles == 0:
        if sum(board) == total_candles:
            return [board]
        return 
    all_solutions = []
    for i in range(index, len(board)):
        cp_board = board[:]
        cp_board[i] = 1
        solution = fill_all_chandeliers_recur(cp_board, i + 1, nb_candles - 1, total_candles)
        if not solution is None: 
            all_solutions.extend(solution)
    return all_solutions

def get_all_possible_chandeliers(n, m):
    board = [0] * int(n)
    all_boards = fill_all_chandeliers_recur(board, 0, m, m)
    return all_boards


def sieve_of_eratosthenes(n):
    A = [True] * n
    A[0] = False
    # A[1] = False
    sqrt_n = int(n ** (1/2))
    for i in range(2, sqrt_n):
        if A[i]:
            j = i ** 2
            while j < n:
                A[j] = False
                j += i
    primes = [i for i, a in enumerate(A) if a]
    return primes


def get_prime_divisors(nb):
    primes = sieve_of_eratosthenes(nb + 1)
    divisors = [p for p in primes if nb % p == 0]
    return divisors

def binomial_coef(n, k):
    up = math.factorial(n)
    down = math.factorial(n - k) * math.factorial(k)
    res = up / down
    return res

def get_common_prime_divisors(n, m):
    n_divisors = get_prime_divisors(n)
    m_divisors = get_prime_divisors(m)

    common_divisors = []
    for n_divisor in n_divisors:
        if n_divisor in m_divisors and n_divisor != 1:
            common_divisors.append(n_divisor)
    print(f"{n = } & {m = }: {common_divisors = }")
    return common_divisors

def solve_768_explicit(n, m):
    print(f"{'~' * 40}")
    common_divisors = get_common_prime_divisors(n, m)
    total_boards = 0
    for c in common_divisors:

        # all_boards = get_all_possible_chandeliers(n // c, m //c)
        n_i = n // c
        m_i = m // c

        nb_sols = binomial_coef(n_i, m_i)
        print(f"For {c = }: {n_i = } & {m_i = } there are {nb_sols = }, with duplicates")
        cd_i = get_common_prime_divisors(n_i, m_i)
        for cc in cd_i:
            if cc != c:
                n_ii = n_i // cc
                m_ii = m_i // cc
                nb_sols_ii = binomial_coef(n_ii, m_ii)
                print(f"\tFor {cc = }: {n_ii = } & {m_ii = } there are {nb_sols_ii = }, with duplicates")
                nb_sols -= nb_sols_ii // 2
        total_boards += nb_sols
        print(f"{c = } {nb_sols =}")


        # print(f"For {c = }, {len(all_boards) = }")
        # total_boards += len(all_boards)
    print(f"{total_boards = }")
    print(f"{'~' * 40}")


def solve_768_iterative(n=24, m=12):
    ret = get_all_possible_chandeliers(n, m)
    good = {}
    for i, sol in enumerate(ret):
        c = get_chandelier_gravity_center(sol)
        if c < 1e-10:
            good[i] = sol
            print(f"{i = } {sol = } {c = }")
    print(f"{len(good.keys()) = }")
    print(f"{len(ret) = }")


examples = [
    {
        "args": [4, 2],
        "return": 2
    },
    {
        "args": [12, 4],
        # 12 = 2 x 2 x 3
        "return": 15
    },
    {
        "args": [36, 6],
        # 36 = 2 x 2 x 3 x 3
        "return": 876
    },
    {
        "args": [360, 20],
        # 360 = 2 x 2 x 2 x 3 x 3 x 5
        "return": -1
    }
]

if __name__ == "__main__":
    n = 24
    m = 12
    solve_768_iterative(n, m)
    solve_768_explicit(n, m)
    # for example in examples:
    #     solve_768_explicit(*example["args"])
    #     print(f"{example['return'] = }")