# -*- coding:utf-8 -*-

class AlipayRequest(object):
    def getApiMethodName(self):
        """获取TOP的API名称
        @return API名称 string
        """
        pass

    def getTextParams(self):
        """获取所有的Key-Value形式的文本请求参数集合。
        期中：
        <url>
          <li>Key: 请求参数名</li>
          <li>Value: 请求参数值</li>
        </url>

        @return 文本请求参数集合 dict{string, string}

        """
        pass

    def getApiVersion(self):
        """得到当前接口的版本
        @return API版本 string
        """
        pass

    def setApiVersion(self, apiVersion):
        """设置当前API的版本信息
        @param apiVersion API版本 string
        """
        pass

    def getTerminalType(self):
        """获取终端类型
        @return 终端信息 string
        """
        pass

    def setTerminalInfo(self, terminalInfo):
        """设置终端信息
        @param terminalType 终端类型 string
        """
        pass

    def getProdCode(self):
        """获取产品码
        @return 产品码  string
        """
        pass

    def setProdCode(self, prodCode):
        """设置产品码
        @param prodCode 产品码 string
        """
        pass

    def getNotifyUrl(self):
        """返回通知地址
        @return 通知地址 string
        """
        pass

    def setNotifyUrl(self, notifyUrl):
        """设置通知地址
        @param notifyUrl 通知地址 string
        """
        pass

    def getReturnUrl(self):
        """返回回跳地址
        @return 回跳地址 string
        """
        pass

    def setReturnUrl(self, returnUrl):
        """设置回跳地址
        @param returnUrl 回跳地址 string
        """
        pass

    def getResponseClass(self):
        """得到当前API的响应结果类型
        @return 相应类型 class
        """
        pass

    def isNeedEncript(self):
        """判断是否需要加密
        @return 是否需要加密 bool
        """
        pass

    def setNeedEncrypt(self, needEncrypt):
        """设置请求是否需要加密
        @param needEncrypt 是否需要加密  bool
        """
        pass

    def getBizModel(self):
        """获取业务实体
        @return 业务实体 object
        """
        pass

    def setBizModel(self, bizModel):
        """设置业务实体，如需要使用此方法，请勿直接设置biz_content
        """
        pass
