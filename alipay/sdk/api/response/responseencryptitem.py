class ResponseEncryptItem(object):
    def __init__(self, respContent, realContent):
        self.respContent = respContent
        self.realContent = realContent

    def getRespContent(self):
        return self.respContent

    def getRealContent(self):
        return self.realContent
