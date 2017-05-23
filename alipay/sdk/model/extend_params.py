# -*- coding:utf-8 -*-

"""扩展信息

"""

class ExtendParams(object):
    def __init__(self):
        self.sysServiceProviderId = ""

    def __json__(self):
        return {
            'sys_service_provider_id': self.self.sysServiceProviderId
            }

    def toString(self):
        return "ExtendParams{sysServiceProviderId='{0}'}"\
               .format(self.sysServiceProviderId)
    
    def getSysServiceProviderId(self):
        return self.sysServiceProviderId

    def setSysServiceProviderId(self, sysServiceProviderId):
        self.sysServiceProviderId = sysServiceProviderId

