# -*- coding:utf-8 -*-

import json

class RequestBuilderEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__json__()

class RequestBuilder(object):
    def __init__(self):
        self.appAuthToken = ""
        self.notifyUrl = ""

    def validate(self):
        """implemented by child class
        验证请求对象
        """
        pass

    def getBizContent(self):
        """implemented by child class
        获取bizCOntent对象，用于下一步转换为json字符串
        """
        pass

    def toJsonString(self):
        """将对象转换为json字符串"""
        return json.dumps(self.getBizContent(), cls=RequestBuilderEncoder)

    def toString(self):
        info = {
            'appAuthToken': self.appAuthToken,
            'notifyUrl': self.notifyUrl
            }

        s = ",".join(["%s=%s" % (k, v) for k, v in info.items()])
        return "RequestBuilder{%s}" % s

    def getAppAuthToken(self):
        return self.appAuthToken

    def setAppAuthToken(self, appAuthToken):
        self.appAuthToken = appAuthToken

    def getNotifyUrl(self):
        return self.notifyUrl

    def setNotifyUrl(self, notifyUrl):
        self.notifyUrl = notifyUrl
    
    
