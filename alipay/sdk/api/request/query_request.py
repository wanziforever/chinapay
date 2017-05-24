# -*- coding:utf-8 -*-

from base_request import AlipayRequest
from sdk.api.response import AlipayTradeQueryResponse

class AlipayTradeQueryRequest(AlipayRequest):
    def __init__(self):
        self.udfParams = {}
        self.apiVersion = "1.0"
        self.bizContent = None
        self.terminalType = ""
        self.terminalInfo = ""
        self.prodCode = ""
        self.notifyUrl = ""
        self.returnUrl = ""
        self.needEncrypt = False
        self.bizModel = None

    def setBizContent(self, bizContent):
        self.bizContent = bizContent

    def getBizContent(self):
        return self.bizContent

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

    def setProdCOde(self, prodCode):
        self.prodCode = prodCode

    def getApiMethodName(self):
        return "alipay.trade.query"

    def getTextParams(self):
        txtParams = {}
        txtParams['biz_content'] = self.bizContent
        if not self.udfParams:
            txtParams.update(self.udfParams)
        return txtParams

    def putOtherTextParam(self, key, value):
        self.udfParams.update({key: value})

    def getResponseClass(self):
        return AlipayTradeQueryResponse

    def isNeedEncrypt(self):
        return self.needEncrypt

    def setNeedEncrypt(self, needEncrypt):
        self.needEncrypt = needEncrypt

    def getBizModel(self):
        return self.bizModel

    def setBizModel(self, bizModel):
        self.bizModel = bizModel
