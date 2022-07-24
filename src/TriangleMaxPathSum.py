from re import L
from colorama import Fore, Style
import numpy as np
import fire

file_path = "./src/number_data/p018_trinagle_4.txt"
file_path = "./src/number_data/p067_triangle_100.txt"
file_path = "./src/number_data/p018_trinagle_15.txt"

class TriangleMaxPathSum():
	def __init__(self, triangle_path=file_path) -> None:
		self.levels = self.read_file(triangle_path)
		self.size = len(self.levels)
		self.levels_max = self.get_max_by_levels()
		self.solution = [0] * self.size
		sums, chcs = self.fill_best_choices()
		self.chcs = chcs
		self.sums = sums

	def read_file(self, triangle_path):
		with open(triangle_path, "r") as f:
			content = f.read()
		levels = []
		for line in content.split("\n"):
			level = []
			for nb in line.split(" "):
				level.append(int(nb))
			levels.append(level)
		return levels


	def get_max_by_levels(self):
		max_by_level = []
		for level in self.levels:
			max_by_level.append(max(level))
		return max_by_level 


	def solve_bruteforce(self, level=0, index=0):
		current = self.levels[level][index]
		if level == self.size - 1:
			return current, [index]
		
		a, a_h = self.solve_bruteforce(
			level=level + 1, 
			index=index
		)

		b, b_h = self.solve_bruteforce(
			level=level + 1, 
			index=index + 1
		)

		if a < b:
			s = b + current
			h = [index] + b_h 
		else:
			s = a + current
			h = [index] + a_h
		return s, h


	def get_line_sums_chcs(self, line):
		sums = []
		chcs = []
		for i, c in enumerate(zip(line[:-1], line[1:])):
			sums.append(max(c))
			chcs.append(np.argmax(c))
		return sums, chcs


	def fill_best_choices(self):
		lvl = self.levels
		sums = []
		chcs = []
		l = self.size - 2

		_sum, _chc = self.get_line_sums_chcs(lvl[-1])
		_sum = [_sum[i] + nb for i, nb in enumerate(lvl[l])]
		sums.append(_sum)
		chcs.append(_chc)
		l -= 1


		while l >= 0:
			_sum, _chc = self.get_line_sums_chcs(_sum)
			_sum = [_sum[i] + nb for i, nb in enumerate(lvl[l])]
			sums.append(_sum)
			chcs.append(_chc)
			l -= 1


		sums = sums[::-1]
		chcs = chcs[::-1]
		return sums, chcs



	def solve(self):
		solution = [0]
		for chc in self.chcs:
			idx = solution[-1]
			idx_add = chc[idx]
			solution.append(idx + idx_add)
		self.solution = solution
		print(self)
		return self.sums[0][0]


	def __str__(self) -> str:
		mxs = 2
		sol = self.solution

		sums = self.sums
		chcs = self.chcs

		l_size = lambda l: (self.size - l) * mxs

		pyramid = ""
		for l, level in enumerate(self.levels):
			pyramid += f"{' ' * l_size(l)}"
			for i, nb in enumerate(level):
				if i == sol[l]:
					pyramid += f"{Fore.GREEN}"
				pyramid += f"{nb:0{mxs}}{' ' * mxs}"
				pyramid += f"{Style.RESET_ALL}"
			pyramid += "\n"
			if l < len(sums):
				pyramid += f"{' ' * l_size(l)}"
				good_idx = {}
				if l > 0:
					good_idx = {i + c for i, c in enumerate(chcs[l - 1])}
				for i, nb in enumerate(chcs[l]):
					if i in good_idx:
						pyramid += f"{Fore.BLUE}"
					else:
						pyramid += f"{Fore.RED}"
					pyramid += f"{'<-' if nb == 0 else '->'}{' ' * mxs}"
					pyramid += f"{Style.RESET_ALL}"
				pyramid += "\n"
		return pyramid


if __name__ == '__main__':
  fire.Fire(TriangleMaxPathSum)
