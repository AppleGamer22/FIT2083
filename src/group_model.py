from typing import List
from random import uniform, randrange
from sys import maxsize
from mesa import Model
from mesa.time import RandomActivation
from .developer_agent import DeveloperAgent
from .bug_agent import BugAgent

class GroupModel(Model):
	def __init__(self, developer_count: int, cve_count_mean: int, total_cve_count, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.cve_count_mean = cve_count_mean
		self.total_cve_count = total_cve_count
		self.developer_count = developer_count
		self.bugs: List[BugAgent] = []
		self.schedule = RandomActivation(self)
		for i in range(self.developer_count):
			self.schedule.add(DeveloperAgent(i, self))

	def step(self):
		for _ in range(100):
			if uniform(0, 1) <= self.cve_count_mean / self.total_cve_count:
				self.bugs.append(BugAgent(randrange(maxsize), self))
