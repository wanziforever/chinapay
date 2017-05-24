import time
from datetime import datetime
from urllib import urlencode, unquote_plus
import requests as HTTPRequest
from base_client import AlipayClient
from sdk.constants import AlipayConstants
from sdk.api.request.requestparametersholder import RequestParameterHolder
from sdk.api.parser import ObjectJsonParser
from sdk.api.response.responseencryptitem import ResponseEncryptItem
from sdk.api.utils import  AlipaySignature
from sdk.utils import stringUtils

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DefaultAlipayClient(AlipayClient):
    def __init__(self, *args):
        """the input can give following argument one by one
        'serverUrl', 'appId', 'privateKey', 'format', 'charset',
        'alipayPublicKey', 'signType', 'encryptKey', 'encryptType'
        """
        AlipayClient.__init__(self)
        self.serverUrl = ""
        self.appId = ""
        self.privateKey = ""
        self.prodCode = ""
        self.format = AlipayConstants.FORMAT_JSON
        self.signType = AlipayConstants.SIGN_TYPE_RSA
        self.encryptType = AlipayConstants.ENCRYPT_TYPE_AES
        self.encryptKey = ""
        self.alipayPublicKey = ""
        self.charset = ""
        # currently, python requests library only support one timeout concept,
        # and will use the connectTimeout
        self.connectTimeout = 3 # seconds
        self.readTimeout = 15

        internals = [
            'serverUrl', 'appId', 'privateKey', 'format', 'charset',
            'alipayPublicKey', 'signType', 'encryptKey', 'encryptType'
            ]

        self.log.debug("DefaultAlipayClient parameters initialized:")
        for arg in args:
            avp = internals.pop(0)
            setattr(self, avp, arg)
            value = getattr(self, avp)
            if len(value) > 80:
                value = "%s ...(ignored)... %s" % (value[:20], value[-20:])
            self.log.debug("%s = %s" %(avp, value))

        self.log.debug("DefaultAlipayClient parameters not initialized")
        self.log.debug(",".join(internals))

        #print "following avps not initialized", ",".join(internals)

    def getRequestHolderWithSign(self, request, accessToken, appAuthToken):
        self.log.debug("DefaultAlipayClient::getRequestHolderWithSign() enter")
        requestHolder = RequestParameterHolder()
        appParams = request.getTextParams()
        #self.log.debug(
        #    "getRequestHolderWithSign() the request params: %s" % appParams)

        if request.getBizModel(): #currently never use the bizModel
            appParams[AlipayConstants.BIZ_CONTENT_KEY] = request.getBizModel()

        # currently, we don't support the encrypt response body, so just don'
        # t care about the encryptType and encryptKey, isNeedEncrypt() always
        # return false.
        if request.isNeedEncrypt():
            AlipayEncrypt.encryptContent(
                appParams.get(AlipayConstrants.BIZ_CONTENT_KEY),
                self.encryptType, self.encryptkey, self.charset)

        if not stringUtils.isEmpty(appAuthToken):
            appParams[AlipayConstants.APP_AUTH_TOKEN] = appAuthToken

        requestHolder.setApplicationParams(appParams)

        #self.log.debug(
        #    "getRequestHolderWithSign() has the application params: %s"
        #    % requestHolder.getApplicationParams())
        
        if stringUtils.isEmpty(self.charset):
            self.charset = AlipayConstants.CHARSET_UTF8

        protocalMustParams = {}
        protocalMustParams[AlipayConstants.METHOD] = request.getApiMethodName()
        protocalMustParams[AlipayConstants.VERSION] = request.getApiVersion()
        protocalMustParams[AlipayConstants.APP_ID] = self.appId
        protocalMustParams[AlipayConstants.SIGN_TYPE] = self.signType
        protocalMustParams[AlipayConstants.TERMINAL_TYPE] = request.getTerminalType()
        protocalMustParams[AlipayConstants.TERMINAL_INFO] = request.getTerminalInfo()
        protocalMustParams[AlipayConstants.NOTIFY_URL] = request.getNotifyUrl()
        protocalMustParams[AlipayConstants.RETURN_URL] = request.getReturnUrl()
        protocalMustParams[AlipayConstants.CHARSET] = self.charset

        if request.isNeedEncrypt(): # currently always return false
            protocalMustParams[AlipayContants.ENCRYPT_TYPE] = self.encryptType

        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        protocalMustParams[AlipayConstants.TIMESTAMP] = ts
        #self.log.debug(
        #    "getRequestHolderWithSign() going to set protocal must params: %s"
        #    % protocalMustParams)
        requestHolder.setProtocalMustParams(protocalMustParams)

        protocalOptParams = {}
        protocalOptParams[AlipayConstants.FORMAT] = self.format
        protocalOptParams[AlipayConstants.ACCESS_TOKEN] = accessToken or ''
        protocalOptParams[AlipayConstants.ALIPAY_SDK] = AlipayConstants.SDK_VERSION
        protocalOptParams[AlipayConstants.PROD_CODE] =  request.getProdCode()
        #self.log.debug(
        #    "getRequestHolderWithSign() going to set protocal opt params: %s"
        #    % protocalOptParams)
        requestHolder.setProtocalOptParams(protocalOptParams)

        if not stringUtils.isEmpty(self.signType):
            signContent = AlipaySignature.getSignatureContent(requestHolder)
            #self.log.debug("signContent: %s" % signContent)
            protocalMustParams[AlipayConstants.SIGN] = AlipaySignature.rsaSign(
                signContent, self.privateKey, self.charset, self.signType)
        else:
            protocalMustParams[AlipayContants.SIGN] = ""

        return requestHolder
      
    def execute(self, request, authToken=None, appAuthToken=None):
        self.log.debug("execute going to do execute")

        # currently only support json format response, so do not need to check
        # the format property. if futher format like XML, will add a XML parser
        self.log.debug("new a json object parser")
        parser = ObjectJsonParser(request.getResponseClass())

        self.log.debug("call doPost to send http request, and get the response")
        rt = self.doPost(request, authToken, appAuthToken)
        if not rt:
            return None

        responseItem = self.encryptResponse(request, rt, parser)
        tRsp = parser.parse(responseItem.getRealContent())
        tRsp.setBody(responseItem.getRealContent())

        #checkResponseSign(request, parser, responseItem.getRespContent(),
        #                  tRsp.isSuccess())
        return tRsp

    def doPost(self, request, accessToken, appAuthToken):
        """ send the http post message, upload file currently not support
        """
        self.log.debug("DefaultAlipayClient::doPost() enter")
        requestHolder = self.getRequestHolderWithSign(request, accessToken,
                                                      appAuthToken)
        url = self.getRequestUrl(requestHolder)
        #self.log.debug("doPost() raw url %s" % unquote_plus(url))
        #self.log.debug("doPost() url %s" % url)
        rsp = None

        # the HTTPRequest is the thirdParty requests module, need code to monitor
        # exceptions for it
        postData = requestHolder.getApplicationParams()

        rsp = HTTPRequest.post(url, data=urlencode(postData),
                               timeout=self.connectTimeout)
        self.log.debug(rsp.content)

        result = {
            'rsp': rsp.content,
            'textParams': requestHolder.getApplicationParams(),
            'protocalMustParams': requestHolder.getProtocalMustParams(),
            'protocalOptParams': requestHolder.getProtocalOptParams(),
            'url': url
            }
        return result

    def encryptResponse(self, request, rt, parser):
        responseBody = rt.get('rsp')
        realBody = None
        if request.isNeedEncrypt(): # currently never goes here
            realBody = parser.encryptSourceData(request, responseBody,
                                                self.format,
                                                self.encryptType,
                                                self.encryptkey,
                                                self.charset)
        else:
            realBody = responseBody

        return ResponseEncryptItem(responseBody, realBody)

    def getRequestUrl(self, requestHolder):
        mustQuery = urlencode(requestHolder.getProtocalMustParams())
        optQuery = urlencode(requestHolder.getProtocalOptParams())
        appQuery = urlencode(requestHolder.getApplicationParams())

        #debugMustQuery = "&".join("{0}={1}".format(k, v) for k, v in requestHolder.getProtocalMustParams().items())
        #debugOptQuery = "&".join("{0}={1}".format(k, v) for k, v in requestHolder.getProtocalOptParams().items())
        #debugAppQuery = "&".join("{0}={1}".format(k, v) for k, v in requestHolder.getApplicationParams().items())
        #
        #debugServerUrl = self.serverUrl + "?" + debugMustQuery + "&" + \
        #                 debugAppQuery + "&" + debugOptQuery
        #self.log.debug("debug url is %s" % debugServerUrl)
        
        
        return self.serverUrl + "?" + mustQuery + "&" + appQuery + "&" + optQuery
