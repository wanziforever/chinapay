# -*- coding:utf-8 -*-

class AlipayParser(object):
    def parse(self, rsp):
        """把响应字符串解释成相应的领域对象。
        @param rsp 响应字符串
        @return 领域对象
        """
        pass

    def getResponseClass(self):
        """获取响应类类型
        """
        pass

    def getSignItem(request, responseBody):
        """获取响应内的签名数据
        @param rsp 响应字符串
        @return
        @throws AlipayApiException
        """
        pass

    def encryptSourceData(request, body, format, encryptType,
                          encryptkey, charset):
        """获取实际串：如果是加密内容则返回内容已经是解密后的实际内容了
        @param request
        @param body
        @param format
        @param encryptType
        @param encryptKey
        @param charset
        @return
        @throws AlipayApiException
        """
        pass
    
