# -*- coding:utf-8 -*-

from base_response import AlipayResponse

class AlipayTradePrecreateResponse(AlipayResponse):
    def __init__(self):
        AlipayResponse.__init__(self)
        # 商户的定的那好
        self.outTradeNo = ""
        # 当前预下单请求生成的二维码码串，可以用二维码生成工具
        # 根据该码串声称对应的二维码。
        self.qrCode = ""

    def setOutTradeNo(self, outTradeNo):
        self.outTradeNo = outTradeNo

    def getOutTradeNo(self):
        return self.outTradeNo

    def setQrCode(self, qrCode):
        self.qrCode = qrCode

    def getQrCode(self):
        return self.qrCode
