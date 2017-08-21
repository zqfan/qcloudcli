#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteNatGatewayRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'DeleteNatGateway', 'vpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_natId(self):
		return self.get_params().get('natId')

	def set_natId(self, natId):
		self.add_param('natId', natId)
