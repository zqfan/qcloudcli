#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreateBmSubnetRequest(Request):

	def __init__(self):
		Request.__init__(self, 'bmvpc', 'qcloudcliV1', 'CreateBmSubnet', 'bmvpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_subnetSet(self):
		return self.get_params().get('subnetSet')

	def set_subnetSet(self, subnetSet):
		self.add_param('subnetSet', subnetSet)

	def get_vlanId(self):
		return self.get_params().get('vlanId')

	def set_vlanId(self, vlanId):
		self.add_param('vlanId', vlanId)

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_subnetSet(self):
		return self.get_params().get('subnetSet')

	def set_subnetSet(self, subnetSet):
		self.add_param('subnetSet', subnetSet)

	def get_vlanId(self):
		return self.get_params().get('vlanId')

	def set_vlanId(self, vlanId):
		self.add_param('vlanId', vlanId)

	def get_dockerFlag(self):
		return self.get_params().get('dockerFlag')

	def set_dockerFlag(self, dockerFlag):
		self.add_param('dockerFlag', dockerFlag)

