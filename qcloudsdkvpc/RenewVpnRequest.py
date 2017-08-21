#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class RenewVpnRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'RenewVpn', 'vpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_vpnGwId(self):
		return self.get_params().get('vpnGwId')

	def set_vpnGwId(self, vpnGwId):
		self.add_param('vpnGwId', vpnGwId)

	def get_period(self):
		return self.get_params().get('period')

	def set_period(self, period):
		self.add_param('period', period)
