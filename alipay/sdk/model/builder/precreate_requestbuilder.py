# -*- coding:utf-8 -*-

from requestbuilder import RequestBuilder

class AlipayTradePrecreateRequestBuilder(RequestBuilder):
    class BizContent(object):
        def __init__(self):
            # 商户网站订单系统中唯一订单号，64个字符以内，只能包含字母、数字、
            # 下划线，需保证商户系统端不能重复，建议通过数据库sequence生成。
            self.outTradeNo = ""

            # 卖家支付宝账号ID，用于支持一个签约账号下支持打款到不同的收款账号，
            #（打款到sellerId对应的支付宝账号。如果该字段为空，则默认为与支付宝
            # 的商户的PID，也就是appid对应的PID。
            self.sellerId = ""
            
            # 订单总金额，整形，此处单位为元，精确到小数点后2位，不能超过1亿元
            # 如果同时传入了【打折金额】，【不可打折金额】，【订单总金额】三者，
            # 则必须满足如下条件：【订单总金额】=【打折金额】+【不可打折金额】
            self.totalAmount = ""

            # 订单可打折金额，此处单位为元，精确到小数点后2位，可以配合商家平台
            # 配置折扣活动，如果订单部分商品参与打折，可以将部分商品总价填写至
            # 此字段，默认全部商品可打折。
            # 如果该值未传入,但传入了【订单总金额】,【不可打折金额】 则该值默认
            # 为【订单总金额】- 【不可打折金额】
            self.discountableAmount = ""

            # 订单不可打折金额，此处单位为元，精确到小数点后2位，可以配合商家平
            # 台配置折扣活动，如果酒水不参与打折，则将对应金额填写至此字段.
            # 如果该值未传入,但传入了【订单总金额】,【打折金额】,则该值默认为
            # 【订单总金额】-【打折金额】
            self.undiscountableAmount = ""

            # 订单标题，粗略描述用户的支付目的。如“喜士多（浦东店）消费”
            self.subject = ""

            # 订单描述，可以对交易或商品进行一个详细地描述，比如填写"购买商品2件
            # 共15.00元"。
            self.body = ""

            # 商品明细列表，需填写购买商品详细信息
            self.goodsDetailList = []

            # 商户操作员编号，添加此参数可以为商户操作员做销售统计
            self.operatorId = ""

            # 商户门店编号，通过门店和商家后台可以配置精准到门店的折扣信息
            self.storeId = ""

            # 支付宝商家平台中配置的商户门店号
            self.alipayStoreID = ""

            # 商户机具终端编号，当以机具方式接入支付宝时必传
            self.terminalId = ""

            # 业务扩展参数，目前可添加由支付宝分配的系统商编号(通过
            # setSysServiceProviderId方法)
            self.extendParams = None

            # (推荐使用，相对时间) 支付超时时间，5m 5分钟
            self.timeoutExpress = ""

        def toString(self):
            return ("BizContent\{"
                    "outTradeNo='{outTradeNo}', "
                    "sellerId='{sellerId}',"
                    "totalAmount='{totalAmount}', "
                    "discountableAmount='{discountableAmount}',"
                    "undiscountableAmount='{undiscountableAmount}', "
                    "subject='{subject}',"
                    "body='{body}', "
                    "goodsDetailList={goodsDetailList}, "
                    "operatorId='{operatorId}',"
                    "storeId='{storeId}', "
                    "alipayStoreId='{alipayStoreId}', "
                    "terminalId='{terminalId}',"
                    "extendParams={extendParams}, "
                    "timeoutExpress='{timeoutExpress}'\}").format(
                outTradeNo = self.outTradeNo,
                sellerId = self.sellerId,
                totalAmount = self.totalAmount,
                discountableAmount = self.discountableAmount,
                undiscountableAmount = self.undiscountableAmount,
                subject = self.subject,
                body = self.body,
                goodsDetailList = "[" + ",".join(self.goodsDetailList) + "]",
                operatorId = self.operatorId,
                storeId = self.storeId,
                alipayStoreId = self.alipayStoreId,
                terminalId = self.terminalId,
                extendParams = self.extendParams,
                timeoutExpress = self.timeoutExpress
                )
        # finish the BizContent class definition

    def __init__(self):
        self.bizContent = AlipayTradePrecreateRequestBuilder.BizContent()

    def getBizContent(self):
        return self.bizContent

    def validate(self):
        if len(self.bizContent.outTradeNo) == 0:
            raise Exception("out_trade_no should not be NULL!")
        if len(self.bizContent.totalAmount) == 0:
            raise Exception("total_amount should not be NULL!")
        if len(self.bizContent.subject) == 0:
            raise Exception("subject should not be NULL!")
        if len(self.bizContent.storeId) == 0:
            raise Exception("store_id should not be NULL!")

        return True
        
    def toString(self):
        return ("AlipayTradePrecreateRequestBuilder\{"
                "bizContent={bizContent},"
                "super={_super}"
                "\}").format(
            bizContent = self.bizContent.toString(),
            _super = super.toString()
            )

    def getOutTradeNo(self):
        return self.bizContent.outTradeNo

    def setOutTradeNo(self, outTradeNo):
        self.bizContent.outTradeNo = outTradeNo

    def getSellerId(self):
        return self.bizContent.sellerId

    def setSellerId(self, sellerId):
        self.bizContent.sellerId = sellerId

    def getTotalAmount(self):
        return self.bizContent.totalAmount

    def setTotalAmount(self, totalAmount):
        self.bizContent.totalAmount = totalAmount

    def getDiscountableAmount(self):
        return self.bizContent.discountableAmount

    def setDiscountableAmount(self, discountableAmount):
        self.bizContent.discountableAmount = discountableAmount

    def getUndiscountableAmount(self):
        return self.bizContent.undiscountableAmount

    def setUndiscountableAmount(self, undiscountableAmount):
        self.bizContent.undiscountableAmount = undiscountableAmount

    def getSubject(self):
        return self.bizContent.subject

    def setSubject(self, subject):
        self.bizContent.subject = subject

    def getBody(self):
        return self.bizContent.body

    def setBody(self, body):
        self.bizContent.body = body

    def getGoodsDetailList(self):
        return self.bizContent.goodsDetailList

    def setGoodsDetailList(self, goodsDetailList):
        self.bizContent.goodsDetailList = goodsDetailList

    def getOperatorId(self):
        return self.bizContent.operatorId

    def setOperatorId(self, operatorId):
        self.bizContent.operatorId = operatorId

    def getStoreId(self):
        return self.bizContent.storeId

    def setStoreId(self, storeId):
        self.bizContent.storeId = storeId

    def getAlipayStoreId(self):
        return self.bizContent.alipayStoreId

    def setAlipayStoreId(self, alipayStoreId):
        self.bizContent.alipayStoreId = alipayStoreId

    def getTerminalId(self):
        return self.bizContent.terminalId

    def setTerminalId(self, terminalId):
        self.bizContent.terminalId = terminalId

    def getExtendParams(self):
        return self.bizContent.extendParams

    def setExtendParams(self, extendParams):
        self.bizContent.extendParams = extendParams

    def getTimeoutExpress(self):
        return self.bizContent.timeoutExpress

    def setTimeoutExpress(self, timeoutExpress):
        self.bizContent.timeoutExpress = timeoutExpress
        
