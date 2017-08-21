#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreateNamespaceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'CreateNamespace', 'monitor.api.qcloud.com')

	def get_namespace(self):
		return self.get_params().get('namespace')

	def set_namespace(self, namespace):
		self.add_param('namespace', namespace)
