#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import logging
from sdk.model.extend_params import ExtendParams
from sdk.model.goods import newGoods
from sdk.config.configs import Configs
from sdk.model.builder import AlipayTradePrecreateRequestBuilder
from sdk.model.builder import AlipayTradeQueryRequestBuilder
from sdk.service.alipaytradeservice import ClientBuilder
from sdk.model.tradestatus import TradeStatus

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
                    )

log = logging.getLogger("alipayTrade_main")
#log.setLevel(logging.INFO)
#ch = logging.StreamHandler()
#ch.setLevel(logging.INFO)
#formatter=logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#ch.setFormatter(formatter)
#log.addHandler(ch)

def test_trade_precreate():
    pass

Configs.init('zfbinfo.conf')

def dumpResponse(response):
    log.info(response.toString())

def test_trade_precreate():
    # (必填) 商户网站订单系统中唯一订单号，64个字符以内，只能包含字母，
    # 数字，下划线，
    # 需保证商户系统端不能重复，建议通过数据库sequence生成。
    outTradeNo = "tradeprecreate" + \
                 str(int(time.clock() * 1000000) + int(time.time() * 1000))

    # （必填）订单标题，粗略描述用户的支付目的。如“xxx品牌xxx门店当面付扫码消费”
    subject = "xxx品牌xxx门店当面付扫码消费"

    # (必填)订单总金额，单位为元，不能超过1亿元
    # 如果同时传入了【打折金额】，【不可打折金额】，【订单总金额】三者，
    # 则必须满足如下条件：【订单总金额】=【打折金额】+【不可打折金额】
    totalAmount = "0.01"

    # （可选）订单不可打折金额，可以配合商家平台配置折扣活动，如果酒水不参与打折，
    # 则将对应余额填写至此字段。如果该值未传入，但传入了【订单总金额】，【打折金额】
    # 则该值默认为【订单总金额】 - 【打折金额】
    undiscountableAmount = "0.01"

    # 如果该字段为空，则默认为与支付宝签约的商户的PID，
    # 也就是appid对应的PID
    sellerId = ""

    # 订单描述，可以对交易或商品进行一个详细地描述，比如填写“购买商品2件共15.00元”
    body = "购买商品3件共20.00元"

    # 商户操作员变好，添加此参数可以为商户操作员做销售统计
    operatorId = "test_operator_id"

    # （必填）商户门店编号，通过门店号和商家后台可以配置精准到门店的折扣信息
    storeId = "test_store_id"

    # 业务扩展参数，目前可添加由支付宝分配的系统上编号（通过setSysServiceProviderId方法）
    extendParams = ExtendParams()
    extendParams.setSysServiceProviderId("2088100200300400500")

    # 支付超时，定义为120分钟
    timeoutExpress = "120m"

    # 商品明细列表，需填写购买商品详细信息
    goodsDetailList = []
    # 创建一个商品信息，参数含义分别为商品id（使用国标）、名称、单价（单位为分）、
    # 数量，如果需要添加商品类别，详见GoodsDetail
    goods1 = newGoods("goods_id001", "xxx小面包", 1000, 1)
    # 创建好一个商品后添加至商品明细列表
    goodsDetailList.append(goods1)

    # 继续创建并添加第一条商品信息，用户购买的产品为“黑人牙刷”，单价为5.00元，
    # 购买了两件
    goods2 = newGoods("goods_id002", "xxx牙刷", 500, 2)
    goodsDetailList.append(goods2)

    # 创建扫码支付请求builder，设置请求参数
    builder = AlipayTradePrecreateRequestBuilder()
    builder.setSubject(subject)
    builder.setTotalAmount(totalAmount)
    builder.setOutTradeNo(outTradeNo)
    builder.setUndiscountableAmount(undiscountableAmount)
    builder.setSellerId(sellerId)
    builder.setBody(body)
    builder.setOperatorId(operatorId)
    builder.setStoreId(storeId)
    builder.setTimeoutExpress(timeoutExpress)
    builder.setGoodsDetailList(goodsDetailList)
    builder.setExtendParams(extendParams)

    tradeService = ClientBuilder().build()
    result = tradeService.tradePrecreate(builder)

    rsp = result.getTradeStatus()
    
    if rsp == TradeStatus.SUCCESS:
        log.info("支付宝预下单成功：）")
        response = result.getResponse()
        dumpResponse(response)
    elif rsp == TradeStatus.FAILED:
        log.error("支付宝预下单失败！！！")
        response = result.getResponse()
        dumpResponse(response)
    elif rsp == TradeStatus.UNKNOWN:
        log.error("系统异常，预下单状态未知！！！")
        response = result.getResponse()
        dumpResponse(response)
    else:
        log.error("不支持的交易状态， 交易返回异常！！！")
        response = result.getResponse()
        dumpResponse(response)


def test_trade_query():
    # （必填）商户订单号，通过此商户订单号查询当面付的交易状态
    outTradeNo = "trade1494329155453320000"

    # 创建查询请求builder，设置请求参数
    builder = AlipayTradeQueryRequestBuilder()
    builder.setOutTradeNo(outTradeNo)

    tradeService = ClientBuilder().build()
    result = tradeService.queryTradeResult(builder)

    rsp = result.getTradeStatus()

    if rsp == TradeStatus.SUCCESS:
        log.info("查询返回订单支付成功：）")
        response = result.getResponse()
        dumpResponse(response)
    elif rsp == TradeStatus.FAILED:
        log.error("查询返回该订单支付失败或被关闭")
        response = result.getResponse()
        dumpResponse(response)
    elif rsp == TradeStatus.UNKNOWN:
        log.error("系统异常， 订单支付状态未知！！！")
        response = result.getResponse()
        dumpResponse(response)
    else:
        log.error("不支持的交易状态，交易返回异常！！！")
        response = result.getResponse()
        dumpResponse(response)



if __name__ == "__main__":
    test_trade_precreate()
    test_trade_query()
