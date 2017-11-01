# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteLocalSourceIPPortTranslationAclRuleRequest(Request):

    def __init__(self):
        super(DeleteLocalSourceIPPortTranslationAclRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DeleteLocalSourceIPPortTranslationAclRule', 'vpc.api.qcloud.com')

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_translationIPPool(self):
        return self.get_params().get('translationIPPool')

    def set_translationIPPool(self, translationIPPool):
        self.add_param('translationIPPool', translationIPPool)

    def get_aclRules(self):
        return self.get_params().get('aclRules')

    def set_aclRules(self, aclRules):
        self.add_param('aclRules', aclRules)
