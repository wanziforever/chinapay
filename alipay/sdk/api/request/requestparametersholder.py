class RequestParameterHolder(object):
    def __init__(self):
        self.protocalMustParams = {}
        self.protocalOptParams = {}
        self.applicationParams = {}

    def getProtocalMustParams(self):
        return self.protocalMustParams

    def setProtocalMustParams(self, protocalMustParams):
        self.protocalMustParams = protocalMustParams

    def getProtocalOptParams(self):
        return self.protocalOptParams

    def setProtocalOptParams(self, protocalOptParams):
        self.protocalOptParams = protocalOptParams

    def getApplicationParams(self):
        return self.applicationParams

    def setApplicationParams(self, applicationParams):
        self.applicationParams = applicationParams
