from .group_model import GroupModel

class ClosedModel(GroupModel):
	cve_count_mean = 388.304348
	total_windows_cve_count = 4612

	def __init__(self, *args, **kwargs):
		super().__init__(10, ClosedModel.cve_count_mean, ClosedModel.total_windows_cve_count, *args, **kwargs)