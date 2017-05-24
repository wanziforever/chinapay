# -*- coding:utf-8 -*-

from sdk.api.utils import stringUtils

class AlipayResponse(object):
    PREFIX = "_ApiField_"
    def __init__(self):
        self._ApiField_code = ""
        self._ApiField_msg = ""
        self._ApiField_sub_code = ""
        self._ApiField_sub_msg = ""
        self.body = ""
        self.params = {}

    def toString(self):
        avpTuples = []
        for rawAvp in dir(self):
            if not rawAvp.startswith(self.PREFIX):
                continue
            avp = rawAvp.replace(self.PREFIX, '')
            avpTuples.append("{0}={1}".format(avp, getattr(self, rawAvp)))
        return ','.join(avpTuples)

    def getCode(self):
        return self._ApiField_code

    #def setCode(self, code):
    #    self._ApiField_code = code

    def getMsg(self):
        return self._ApiField_msg

    #def setMsg(self, msg):
    #    self._ApiField_msg = msg

    def getSubCode(self):
        return self._ApiField_subCode

    #def setSubCode(self, subCode):
    #    self._ApiField_subCode = subCode

    def getSubMsg(self):
        return self._ApiField_subMsg

    #def setSubMsg(self, subMsg):
    #    self._ApiField_subMsg = subMsg

    def getBody(self):
        return self.body

    def setBody(self, body):
       self.body = body

    def getParams(self):
        return self.params

    def setParams(self, params):
        self.params = params

    def isSuccess(self):
        return stringUtils.isEmpty(self._ApiField_subCode)

    def getTopExpectTag(self):
        pass
