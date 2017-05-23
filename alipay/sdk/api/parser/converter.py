class Converter(object):
    def toResponse(self, rsp, clazz):
        """把字符串转换为响应对象。
        @param <T> 领域泛型
        @param rsp 响应字符串
        @param clazz 领域类型
        @return 响应对象
        """
        pass

    def getSignItem(self, request, responseBody):
        """获取响应内的签名数据
        @param request
        @param responseBody
        @return
        """
        pass

    def encryptSourceData(self, request, body, format, encryptType,
                          encryptKey, charset):
        """获取解密后的响应内的真实内容
        @param request
        @param body
        @param format
        @param encryptType
        @param encryptKey
        @param charset
        @return
        """
        pass
    
    
        
