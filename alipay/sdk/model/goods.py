# -*- coding:utf-8 -*-

"""商品明细
"""

class GoodsDetail(object):
    def __init__(self):
        # 商品编号（国标）
        self.goodsId = ""
        self.alipayGoodsId = ""
        
        # 商品名称
        self.goodsName = ""

        # 商品数量
        self.quantity = 0

        # 商品价格，此处单位为元，精确到小数点后2位
        self.price = ""

        # 商品类别
        self.goodsCategory = ""

        # 商品详情
        self.body = ""

    def __json__(self):
        return {
            'goods_id': self.goodsId,
            'alipay_goods_id': self.alipayGoodsId,
            'goods_name': self.goodsName,
            'goods_category': self.goodsCategory
            }
        
    def toString(self):
        info = {"goodsId": self.goodsId,
                "alipayGoodsId": self.alipayGoodsId,
                "goodsName": self.goodsName,
                "quantity": self.quantity,
                "price": self.price,
                "goodsCategory": self.goodsCategory,
                "body": self.body}

        s = ",".join(["%s=%s" % (k, v) for k, v in info.items()])
        return "GoodsDetail{%s}" % s
        
        
    def getGoodId(self):
        return self.goodsId
    
    def setGoodsId(self, goodsId):
        self.goodsId = goodsId

    def getAlipayGoodsId(self):
        return self.alipayGoodsId

    def setAlipayGoodsId(alipayGoodsId):
        self.alipayGoodsId = alipayGoodsId

    def getGoodsName(self):
        return self.goodsName

    def setGoodsName(self, goodsName):
        self.goodsName = goodsName

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        # intut is 
        self.price = price

    def getGoodsCategory(self):
        return self.goodsCategory

    def setGoodsCategory(self, goodsCategory):
        self.goodsCategoyr = goodsCategory

    def getBody(self):
        return self.body

    def setBody(self, body):
        self.body = body
    
def newGoods(goodsId, goodsName, price, quantity):
    # check the price validation, quantity should be a integer
    info = GoodsDetail()
    info.setGoodsId(goodsId)
    info.setGoodsName(goodsName)
    info.setPrice(price)
    info.setQuantity(quantity)
    return info
