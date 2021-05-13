from group_model import GroupModel

class OpenModel(GroupModel):
	developer_count = 10
	cve_count_mean = 200.521739
	total_linux_cve_count = 4612

	def __init__(self, *args, **kwargs):
		super().__init__(10, OpenModel.cve_count_mean, OpenModel.total_linux_cve_count, *args, **kwargs)