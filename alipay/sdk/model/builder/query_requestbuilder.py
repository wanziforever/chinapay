# -*- coding:utf-8 -*-

from requestbuilder import RequestBuilder

class AlipayTradeQueryRequestBuilder(RequestBuilder):
    class BizContent(object):
        def __init__(self):
            self.tradeNo = ""
            self.outTradeNo = ""

        def __json__(self):
            return {
                'trade_no': self.tradeNo,
                'out_trade_no': self.outTradeNo
                }

        def toString(self):
            return ("BizContent\{"
                    "tradeNo='{tradeNo}',"
                    "outTradeNo='{outTradeNo}'\}").format(
                tradeNo = self.tradeNo,
                outTradeNo = self.outTradeNo
                )

    def __init__(self):
        RequestBuilder.__init__(self)
        self.bizContent = AlipayTradeQueryRequestBuilder.BizContent()

    def getBizContent(self):
        return self.bizContent

    def validate(self):
        if len(self.bizContent.tradeNo) == 0 and \
               len(self.bizContent.outTradeNo) == 0:
            print "====", self.bizContent.tradeNo
            print "====", self.bizContent.outTradeNo
            raise Exception("tradeNo and outTradeNo cannot both be NULL!")
        return True

    def toString(self):
        return ("AlipayTradeQueryRequestBuilder\{"
                "bizContent={bizContent},"
                "super={_super}"
                "\}").format(
            bizContent = self.bizContent.toString(),
            _super = super.toString
            )

    def setAppAuthToken(self, appAuthToken):
        super.setAppAuthToken(appAuthToken)

    def setNotifyUrl(self, notifyUrl):
        super.setNotifyUrl(notifyUrl)

    def getTradeNo(self):
        return self.bizContent.TradeNo

    def setTradeNo(self, tradeNo):
        self.bizContent.tradeNo = tradeNo

    def getOutTradeNo(self):
        return self.bizContent.outTradeNo

    def setOutTradeNo(self, outTradeNo):
        self.bizContent.outTradeNo = outTradeNo

