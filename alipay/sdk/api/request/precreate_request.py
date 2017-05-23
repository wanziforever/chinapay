# -*- coding:utf-8 -*-

from base_request import AlipayRequest
from sdk.api.response.precreate_response import AlipayTradePrecreateResponse

class AlipayTradePrecreateRequest(AlipayRequest):
    def __init__(self):
        # add user-edfined text parameters
        self.udfParams = {}
        self.apiVersion = "1.0"
        self.bizContent = ""
        self.terminalType = ""
        self.terminalInfo = ""
        self.prodCode = ""
        self.notifyUrl = ""
        self.returnUrl = ""
        self.needEncrypt = False
        self.bizModel = None

    def getBizContent(self):
        return self.bizContent
    
    def setBizContent(self, bizContent):
        self.bizContent = bizContent;

    def getNotifyUrl(self):
        return self.notifyUrl
    
    def setNotifyUrl(self, notifyUrl):
        self.notifyUrl = notifyUrl

    def getReturnUrl(self):
        return self.returnUrl

    def setReturnUrl(self, returnUrl):
        self.returnUrl = returnUrl

    def getApiVersion(self):
        return self.apiVersion

    def setApiVersion(self, apiVersion):
        self.apiVersion = apiVersion

    def getTerminalType(self):
        return self.terminalType

    def setTerminalType(self, terminalType):
        self.terminalType = terminalType

    def getTerminalInfo(self):
        return self.terminalInfo

    def setTerminalInfo(self, terminalInfo):
        self.terminalInfo = terminalInfo

    def getProdCode(self):
        return self.prodCode

    def setProdCode(self, prodCode):
        self.prodCode = prodCode

    def getApiMethodName(self):
        return "alipay.trade.precreate"

    def getTextParams(self):
        textParams = {}
        textParams['biz_content'] = self.bizContent
        if not self.udfParams:
            textParams.update(self.udfParams)
        return textParams

    def putOtherTextParam(self, key, value):
        self.udfParams.update({key: value})

    def getResponseClass(self):
        return AlipayTradePrecreateResponse

    def isNeedEncrypt(self):
        return self.needEncrypt

    def setNeedEncrypt(self, needEncrypt):
        self.needEncrypt = needEncrypt

    def getBizModel(self):
        return self.bizModel

    def setBizModel(self, bizModel):
        self.bizModel = bizModel
