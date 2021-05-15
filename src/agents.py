from __future__ import annotations
from typing import List
from random import uniform, choice


class Developer:
	bug_del_rate_linux = 128.153271 / 4612
	bug_del_rate_windows = 330.674714 / 8931

	def __init__(self, uid: int, team_size: int, bug_pool: List[Bug]):
		self.bug_uids: List[int] = []
		self.uid = uid
		self.bug_pool = bug_pool
		self.team_size = team_size
		self.edges_count = 0

	def tick(self):
		for _ in range(100):
			is_in_open_group = uniform(0, 1) <= Developer.bug_del_rate_linux
			is_in_closed_group = uniform(0, 1) <= Developer.bug_del_rate_windows
			if len(self.bug_pool) > 0 and len(self.bug_uids) < 3 and (is_in_open_group or is_in_closed_group):
				bug: Bug = choice(self.bug_pool)
				self.bug_uids.append(bug.uid)
				bug.edges_count += 1
			to_remove: List[int] = []
			for uid in self.bug_uids:
				if not any(bug.uid == uid for bug in self.bug_pool):
					to_remove.append(uid)
			for uid in to_remove:
				self.bug_uids.remove(uid)

class Bug:
	def __init__(self, uid: int, developer_count: int, bug_pool: List[Bug], bug_deleted: List[int]):
		self.uid = uid
		self.bug_pool = bug_pool
		self.bug_deleted = bug_deleted
		self.developer_count = developer_count
		self.edges_count = 0

	def __eq__(self, other_uid: int) -> bool:
		return self.uid == other_uid

	def tick(self, step: int):
		if self.edges_count >= 4:
			self.bug_pool.remove(self)
			self.bug_deleted[step] += 1
