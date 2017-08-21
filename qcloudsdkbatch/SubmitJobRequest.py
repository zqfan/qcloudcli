#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class SubmitJobRequest(Request):

	def __init__(self):
		Request.__init__(self, 'batch', 'qcloudcliV1', 'SubmitJob', 'batch.api.qcloud.com')

	def get_Placement(self):
		return self.get_params().get('Placement')

	def set_Placement(self, Placement):
		self.add_param('Placement', Placement)

	def get_Job(self):
		return self.get_params().get('Job')

	def set_Job(self, Job):
		self.add_param('Job', Job)

	def get_Version(self):
		return self.get_params().get('Version')

	def set_Version(self, Version):
		self.add_param('Version', Version)
