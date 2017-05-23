class ContentBuilder(object):
    def __init__(self):
        self.appAuthToken = ""
        self.notifyUrl = ""

    def setAppAuthToken(self, appAuthToken):
        self.appAuthTOken = appAuthToken

    def setNotifyUrl(self, notifyUrl):
        self.notifyUrl = notifyUrl

    def getAppAuthToken(self):
        return self.appAuthToken

    def getNotifyUrl(self):
        return self.notifyUrl
