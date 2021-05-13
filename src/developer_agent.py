from typing import Set, Union
from random import uniform, choice
from mesa import Agent
from .bug_agent import BugAgent
from .open_model import OpenModel
from .closed_model import ClosedModel

class DeveloperAgent(Agent):
	bug_del_rate_linux = 128.153271 / OpenModel.total_linux_cve_count
	bug_del_rate_windows = 330.674714 / ClosedModel.total_windows_cve_count

	def __init__(self, unique_id: int, model: Union[OpenModel, ClosedModel]):
		super().__init__(unique_id, model)
		self.bugs: Set[BugAgent] = {}

	def step(self):
		for i in range(100):
			is_in_open_group = isinstance(self.model, OpenModel) and uniform(0, 1) <= DeveloperAgent.bug_del_rate_linux
			is_in_closed_group = isinstance(self.model, ClosedModel) and uniform(0, 1) <= DeveloperAgent.bug_del_rate_windows
			if is_in_open_group or is_in_closed_group:
				bug = choice(OpenModel.bugs)
				self.bugs.add(bug.unique_id)
				bug.edges_count += 1