from pandas import DataFrame
from models import OpenGroup, ClosedGroup

open_group_data = {}
closed_group_data = {}

for i in range(20):
	print(f"Trial #{i + 1}")
	open_group = OpenGroup(25)
	closed_group = ClosedGroup(25)
	for _ in range(10000):
		open_group.tick()
		closed_group.tick()
	print(sum(open_group.bug_deleted))
	open_group_data[f"{i + 1}"] = open_group.bug_deleted
	print(sum(closed_group.bug_deleted))
	closed_group_data[f"{i + 1}"] = closed_group.bug_deleted

df_open = DataFrame(open_group_data)
df_open.to_csv("docs/open.csv")

df_closed = DataFrame(closed_group_data)
df_closed.to_csv("docs/closed.csv")
