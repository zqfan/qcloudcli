#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class RecordLifeCycleHookTimeoutRequest(Request):

	def __init__(self):
		Request.__init__(self, 'scaling', 'qcloudcliV1', 'RecordLifeCycleHookTimeout', 'scaling.api.qcloud.com')

	def get_scalingGroupId(self):
		return self.get_params().get('scalingGroupId')

	def set_scalingGroupId(self, scalingGroupId):
		self.add_param('scalingGroupId', scalingGroupId)

	def get_lifeCycleHookId(self):
		return self.get_params().get('lifeCycleHookId')

	def set_lifeCycleHookId(self, lifeCycleHookId):
		self.add_param('lifeCycleHookId', lifeCycleHookId)

	def get_scalingInstanceId(self):
		return self.get_params().get('scalingInstanceId')

	def set_scalingInstanceId(self, scalingInstanceId):
		self.add_param('scalingInstanceId', scalingInstanceId)

	def get_recordTimeout(self):
		return self.get_params().get('recordTimeout')

	def set_recordTimeout(self, recordTimeout):
		self.add_param('recordTimeout', recordTimeout)
