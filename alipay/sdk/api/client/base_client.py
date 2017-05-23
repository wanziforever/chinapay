import logging

class AlipayClient(object):
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        
    def execute(self, request, accessToken=None, appAuthToken=None):
        pass

    def pageExecute(self, request):
        pass

    def sdkExecute(self, request):
        pass

    def parseAppSyncResult(result, requestClass):
        pass
    
