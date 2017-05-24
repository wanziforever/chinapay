# -*- coding:utf-8 -*-

from base_response import AlipayResponse

class AlipayTradePrecreateResponse(AlipayResponse):
    def __init__(self):
        AlipayResponse.__init__(self)
        # 商户的定的那好
        self._ApiField_out_trade_no = ""
        # 当前预下单请求生成的二维码码串，可以用二维码生成工具
        # 根据该码串声称对应的二维码。
        self._ApiField_qr_code = ""

    #def setOutTradeNo(self, outTradeNo):
    #    self._ApiField_outTradeNo = outTradeNo

    def getOutTradeNo(self):
        return self._ApiField_out_trade_no

    #def setQrCode(self, qrCode):
    #    self._ApiField_qrCode = qrCode

    def getQrCode(self):
        return self._ApiField_qr_code

    def getTopExpectTag(self):
        return 'alipay_trade_precreate_response'
