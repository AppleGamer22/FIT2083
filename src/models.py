from typing import List
from sys import maxsize
from random import uniform, randrange
from agents import Bug, Developer

class Group:
	def __init__(self, developer_count: int, cve_count_mean: int, total_cve_count: int):
		self.cve_count_mean = cve_count_mean
		self.total_cve_count = total_cve_count
		self.bug_deleted = [0]
		self.developers: List[Developer] = []
		self.bugs: List[Bug] = []
		for i in range(developer_count):
			self.developers.append(Developer(i, self.bugs))

	def tick(self):
		self.bug_deleted.append(0)
		for bug in self.bugs:
			bug.tick(len(self.bug_deleted) - 1)
		for developer in self.developers:
			developer.tick()
		for _ in range(100):
			if uniform(0, 1) <= self.cve_count_mean / self.total_cve_count:
				self.bugs.append(Bug(randrange(maxsize), len(self.developers), self.bugs, self.bug_deleted))


class OpenGroup(Group):
	developer_count = 10
	cve_count_mean = 200.521739
	total_linux_cve_count = 4612

	def __init__(self, developer_count: int):
		super().__init__(developer_count, OpenGroup.cve_count_mean, OpenGroup.total_linux_cve_count)

class ClosedGroup(Group):
	cve_count_mean = 388.304348
	total_windows_cve_count = 8931

	def __init__(self):
		super().__init__(10, ClosedGroup.cve_count_mean, ClosedGroup.total_windows_cve_count)

if __name__ == "__main__":
	open_model = OpenGroup(50)
	for _ in range(1000):
		open_model.tick()
		print(open_model.bug_deleted[-1])