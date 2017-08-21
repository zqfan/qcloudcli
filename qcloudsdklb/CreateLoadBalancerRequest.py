#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreateLoadBalancerRequest(Request):

	def __init__(self):
		Request.__init__(self, 'lb', 'qcloudcliV1', 'CreateLoadBalancer', 'lb.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_subnetId(self):
		return self.get_params().get('subnetId')

	def set_subnetId(self, subnetId):
		self.add_param('subnetId', subnetId)

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

	def get_loadBalancerType(self):
		return self.get_params().get('loadBalancerType')

	def set_loadBalancerType(self, loadBalancerType):
		self.add_param('loadBalancerType', loadBalancerType)

	def get_loadBalancerName(self):
		return self.get_params().get('loadBalancerName')

	def set_loadBalancerName(self, loadBalancerName):
		self.add_param('loadBalancerName', loadBalancerName)

	def get_domainPrefix(self):
		return self.get_params().get('domainPrefix')

	def set_domainPrefix(self, domainPrefix):
		self.add_param('domainPrefix', domainPrefix)

	def get_number(self):
		return self.get_params().get('number')

	def set_number(self, number):
		self.add_param('number', number)

	def get_forward(self):
		return self.get_params().get('forward')

	def set_forward(self, forward):
		self.add_param('forward', forward)

	def get_ispId(self):
		return self.get_params().get('ispId')

	def set_ispId(self, ispId):
		self.add_param('ispId', ispId)
