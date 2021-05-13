from __future__ import annotations
from mesa import Agent
from .group_model import GroupModel

class BugAgent(Agent):
	def __init__(self, unique_id: int, model: GroupModel):
		super().__init__(unique_id, model)
		self.model = model
		self.edges_count = 0
		self.step_count = 0

	def __eq__(self, other: BugAgent) -> bool:
		return self.edges_count == other.edges_count

	def step(self):
		self.step_count += 1
		if self.edges_count > 5:
			self.model.bugs.remove(self)