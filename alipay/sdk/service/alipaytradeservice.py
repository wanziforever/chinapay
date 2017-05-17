# -*- coding:utf-8 -*-
from sdk.config.conigs import Configs
from sdk.utils import stringUtils


class ClientBuilder(object):
    def __init__(self):
        self.gatewayUrl = ""
        self.appid = ""
        self.privateKey = ""
        self.format = ""
        self.charset = ""
        self.alipayPublicKey = ""
        self.signType = ""

    def build(self):
        if stringUtils.isEmpty(self.gatewayUrl):
            self.gatewayUrl = Configs.gateOpenApiDomain()

        if stringUtils.isEmpty(self.appid):
            self.appid = Configs.getAppid()

        if stringUtils.isEmpty(self.privateKey):
            self.privateKey = Configs.getPrivateKey()

        if stringUtils.isEmpty(self.format):
            self.format = "json"

        if stringUtils.isEmpty(self.charset):
            self.charset = "utf-8"

        if stringUtils.isEmpty(self.signType):
            self.signType = Configs.getSignType()

    def setAlipayPublicKey(self, alipayPublicKey):
        self.alipayPublicKey = alipayPublicKey

    def setAppid(self, appid):
        self.appid = appid

    def setCharset(self, charset):
        self.charset = charset

    def setFormat(self, _format):
        self.format = _format

    def setGatewayUrl(self, gatewayUrl):
        self.gatewayUrl = gatewayUrl

    def setPrivateKey(self, privateKey):
        self.privateKey = privateKey

    def setSignType(self, signType):
        self.signType = signType

    def getAlipayPublicKey(self):
        return self.alipayPublicKey

    def getSignType(self):
        return self.signType

    def getAppid(self):
        return self.appid

    def getCharset(self):
        return self.charset

    


class AlipayTradeService(object):
    pass
