"""扩展信息

"""

class ExtendParams(object):
    def __init__(self):
        self.sysServiceProviderId = ""

    def toString(self):
        return "ExtendParams{sysServiceProviderId='{0}'}"\
               .format(self.sysServiceProviderId)
    
