import fire
from src.problems import all_problems
import numpy as np


def solve_problem(problem_number: int):
	fn = all_problems[problem_number]
	solution = fn()
	return solution


if __name__ == '__main__':
  fire.Fire(solve_problem)
