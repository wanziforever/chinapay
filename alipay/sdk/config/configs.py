# -*- coding:utf-8 -*-

import ConfigParser
import StringIO
import functools
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

class Configs(object):
    openApiDomain = ""
    mcloudApiDomain = ""
    pid = ""
    appid = ""
    privateKey = ""
    publicKey = ""
    alipayPublicKey = ""
    signType = ""
    maxQueryRetry = 0
    queryDuration = 0
    maxCancelRetry = 0
    cancelDuration = 0
    heartbeatDelay = 0
    heartbeatDuration = 0

    def __init__(self):
        pass
    
    @classmethod
    def init(cls, filePath):
        with open(filePath) as fd:
            config_str = ('[root]\n' + fd.read()).encode('utf-8')

        fp = StringIO.StringIO(config_str)
        configs = ConfigParser.RawConfigParser()
        configs.readfp(fp)
        configs = functools.partial(configs.get, 'root')

        cls.openApiDomain = configs('open_api_domain')
        cls.mcloudApiDomain = configs('mcloud_api_domain')

        cls.pid = configs('pid')
        cls.appid = configs('appid')
        
        # RSA
        cls.privatekey = configs('private_key')
        cls.publickey = configs('public_key')
        cls.alipayPublicKey = configs('alipay_public_key')
        cls.signType = configs('sign_type')

        # 查询参数
        cls.maxQueryRetry = configs('max_query_retry')
        cls.queryQuration = configs('query_duration')
        cls.maxCancelRetry = configs('max_cancel_retry')
        cls.cancelDuration = configs('cancel_duration')

        # 交易保障调度县城
        cls.heartbeatDelay = configs('heartbeat_delay')
        cls.hearbeatDuration = configs('heartbeat_duration')

    @classmethod
    def description(cls):
        return ("configs\{"
                "支付宝openapi网关：{openapi}\n"
                "支付宝mcloudapi网关域名：{mcloudApiDomain}\n"
                "pid: {pid}\n"
                "appid: {appid}\n"
                "商户RSA私钥：{privateKey}\n"
                "商户RSA公钥：{publicKey}\n"
                "支付宝RSA公钥：{alipayPublicKey}\n"
                "签名类型: {signType}\n"
                "查询重试次数：{queryRetry}\n"
                "查询间隔（毫秒）：{queryDuration}\n"
                "撤销尝试次数：{maxCancelRetry}\n"
                "撤销重试间隔（毫秒）：{cancelDuration}\n"
                "交易保障调度延迟（秒）：{heartbeatDelay}\n"
                "交易保障调度间隔（秒）：{heartbeatDuration}\n"
                "\}"
                ).format(
            openapi = cls.openApiDomain,
            mcloudApiDomain = cls.openApiDomain,
            pid = cls.pid,
            appid = cls.appid,
            privateKey = cls.privateKey,
            publicKey = cls.publicKey,
            alipayPublicKey = cls.alipaypublicKey,
            signType = cls.signType,
            queryRetry = cls.maxQueryRetry,
            queryDuration = cls.queryDuration,
            maxCancelRetry = cls.maxcancelRetry,
            cancelDuration = cls.cancelDuration,
            heartbeatDelay = cls.heartbeatDelay,
            heartbeatDuration = cls.heatbeatDuration,
            )
    @classmethod
    def getOpenApiDomain(cls):
        return cls.openApiDomain

    @classmethod
    def getMcloudApiDomain(cls):
        return cls.mcloudApiDomain

    @classmethod
    def setMcloudApiDomain(cls, mcloudApiDomain):
        cls.mcloudApiDomain = mcloudApiDomain

    @classmethod
    def getPid(cls):
        return cls.pid

    @classmethod
    def getAppid(cls):
        return cls.appid

    @classmethod
    def getPrivateKey(cls):
        return cls.privatekey

    @classmethod
    def getPublicKey(cls):
        return cls.publicKey

    @classmethod
    def getAlipayPublicKey(cls):
        return cls.alipayPublicKey

    @classmethod
    def getSignType(cls):
        return cls.signType

    @classmethod
    def getMaxQueryRetry(cls):
        return cls.maxQueryRetry

    @classmethod
    def getQueryDuration(cls):
        return cls.queryDuration

    @classmethod
    def getMaxCancelRetry(cls):
        return cls.maxCancelRetry

    @classmethod
    def getCancelDuration(cls):
        return cls.cancelDuration

    @classmethod
    def setOpenApiDomain(cls, openApiDomain):
        cls.openApiDomain = openApiDomain

    @classmethod
    def setPid(cls, pid):
        cls.pid = pid

    @classmethod
    def setAppid(cls, appid):
        cls.appid = appid

    @classmethod
    def setPrivateKey(cls, privateKey):
        cls.privateKey = privateKey

    @classmethod
    def setPublicKey(cls, publicKey):
        cls.publicKey = publicKey

    @classmethod
    def setAlipayPublicKey(cls, alipayPublicKey):
        cls.aliPublicKey = alipayPublicKey

    @classmethod
    def setSignType(cls, signType):
        cls.signType = signType

    @classmethod
    def setMaxQueryRetry(cls, maxQueryRetry):
        cls.maxQueryRetry = maxQueryRetry

    @classmethod
    def setQueryDuration(cls, queryDuration):
        cls.queryDuration = queryDuration

    @classmethod
    def setMaxCancelRetry(cls, maxCancelRetry):
        cls.maxCancelRetry = maxCancelRetry

    @classmethod
    def setCancelDuration(cls, cancelDuration):
        cls.cancelDuration = cancelDuration

    @classmethod
    def getHeartbeatDelay(cls):
        return cls.heartbeatDelay

    @classmethod
    def setHeartbeatDelay(cls, heartbeatDelay):
        cls.heartbeatDelay = heartbeatDelay

    @classmethod
    def getHeartbeatDuration(cls):
        return cls.heartbeatDuration

    @classmethod
    def setHeartbeatDuration(cls, heartbeatDuration):
        cls.heartbeatDuration = heartbeatDuration
