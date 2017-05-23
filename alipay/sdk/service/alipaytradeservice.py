# -*- coding:utf-8 -*-

from sdk.config.configs import Configs
from sdk.config.constants import Constants
from sdk.utils import stringUtils
from sdk.service.absalipayserver import AbsAlipayService
from sdk.api.request.precreate_request import AlipayTradePrecreateRequest
from sdk.api.client import DefaultAlipayClient
from sdk.model.result import AlipayF2FPrecreateResult
from sdk.model.tradestatus import TradeStatus


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
            self.gatewayUrl = Configs.getOpenApiDomain()

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

        return AlipayTradeService(self)

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

    def getFormat(self):
        return self.format

    def getGatewayUrl(self):
        return self.gatewayUrl

    def getPrivateKey(self):
        return self.privateKey


class AlipayTradeService(AbsAlipayService):
    def __init__(self, clientBuilder):

        AbsAlipayService.__init__(self)
        if stringUtils.isEmpty(clientBuilder.getGatewayUrl()):
            raise Exception("gatewayUrl should not be NULL")

        if stringUtils.isEmpty(clientBuilder.getAppid()):
            raise Exception("appid should not be NULL!")

        if stringUtils.isEmpty(clientBuilder.getPrivateKey()):
            raise Exception("privateKey should not be NULL!")

        if stringUtils.isEmpty(clientBuilder.getFormat()):
            raise Exception("format should not be NULL!")

        if stringUtils.isEmpty(clientBuilder.getCharset()):
            raise Exception("alipayPublicKey should not be NULL!")

        if stringUtils.isEmpty(clientBuilder.getSignType()):
            raise Exception("signType should not be NULL!")

        self.client = DefaultAlipayClient(clientBuilder.getGatewayUrl(),
                                          clientBuilder.getAppid(),
                                          clientBuilder.getPrivateKey(),
                                          clientBuilder.getFormat(),
                                          clientBuilder.getCharset(),
                                          clientBuilder.getAlipayPublicKey(),
                                          clientBuilder.getSignType())

    def queryTradeResult(self, builder):
        response = tradeQuery(builder)
        result = AlipayF2FQueryResult(response)
        if self.querySuccess(response):
            # 查询返回该订单交易支付成功
            result.setTradeStatus(TradeStatus.SUCCESS)
        elif self.tradeError(response):
            # 查询发生异常，交易状态未知
            result.setTradeStatus(TradeStatus.UNKNOWN)
        else:
            # 其他情况均表明该订单号交易失败
            result.setTradeStatus(TradeStatus.FAILED)
        return result
    
    def tradePrecreate(self, builder):
        self.validateBuilder(builder)
        request = AlipayTradePrecreateRequest()
        request.setNotifyUrl(builder.getNotifyUrl())
        request.putOtherTextParam("app_auth_token", builder.getAppAuthToken())
        request.setBizContent(builder.toJsonString())
        self.log.info("trade.precreate bizContent:" + request.getBizContent())

        response = self.getResponse(self.client, request)
        result = AlipayF2FPrecreateResult(response)
        if response is not None and Constants.SUCCESS == response.getCode():
            # 预下单交易成功
            result.setTradeStatus(TradeStatus.SUCCESS)
        elif self.tradeError(response):
            # 预下单发生异常，状态未知
            result.setTradeStatus(TradeStatus.UNKNOWN)
        else:
            # 其他情况表明该预下单明确失败
            result.setTradeStatus(TradeStatus.FAILED)

        return result

    def tradePay(self, builder):
        pass
    
    def tradeQuery(self, builder):
        pass

    def tradeRefund(self, builder):
        pass

    # 根据查询结果queryResponse判断交易是否支付成功，如果支付成功则更新
    # result并返回，如果不成功则调用撤销
    def checkQueryAndCancel(self, outTradeNo, appAuthToken,
                            result, queryResponse):
        pass

    # 根据外部订单号outTradeNo撤销订单
    def tradeCancel(self, builder):
        pass

    # 轮询查询订单支付结果
    def loopQueryResult(self, builder):
        pass

    # 判断是否停止查询
    def stopQuery(self, response):
        pass

    # 根据外部订单号outTradeNo撤销订单
    def cancelPayResult(self, builder):
        pass

    # 异步撤销
    def asyncCancel(self, builder):
        pass

    # 将查询应答转换为支付应答
    def toPayResponse(self, response):
        pass

    # 撤销需要重试
    def needRetry(self, response):
        pass

    # 查询返回“支付成功”
    def querySuccess(self, response):
        pass

    # 撤销返回“撤销成功”
    def cancelSuccess(self, response):
        return response is not None and Constants.SUCCESS == response.getCode()

    # 交易异常，或发生系统错误
    def tradeError(self, response):
        return response is None or Constants.ERROR == response.getCode()
        
