import time
from datetime import datetime
from urllib import urlencode, unquote
import requests as HTTPRequest
from base_client import AlipayClient
from sdk.constants import AlipayConstants
from sdk.api.request.requestparametersholder import RequestParameterHolder
from sdk.api.parser import ObjectJsonParser
from sdk.api.response.responseencryptitem import ResponseEncryptItem
from sdk.api.utils import  AlipaySignature
from sdk.utils import stringUtils

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
        self.sign_type = AlipayConstants.SIGN_TYPE_RSA
        self.encryptType = AlipayConstants.ENCRYPT_TYPE_AES
        self.encryptKey = ""
        self.alipayPublicKey = ""
        self.charset = ""
        self.connectTimeout = 3000
        self.readTimeout = 15000

        internals = [
            'serverUrl', 'appId', 'privateKey', 'format', 'charset',
            'alipayPublicKey', 'signType', 'encryptKey', 'encryptType'
            ]
        print args
        self.log.debug("DefaultAlipayClient parameters initialized:")
        for arg in args:
            avp = internals.pop(0)
            setattr(self, avp, arg)
            self.log.debug("%s = %s(%s)" %(avp, getattr(self, avp), arg))

        self.log.debug("DefaultAlipayClient parameters not initialized")
        self.log.debug(",".join(internals))

        #print "following avps not initialized", ",".join(internals)

    def getRequestHolderWithSign(self, request, accessToken, appAuthToken):
        self.log.debug("DefaultAlipayClient::getRequestHolderWithSign() enter")
        requestHolder = RequestParameterHolder()
        appParams = request.getTextParams()
        self.log.debug("DefaultAlipayClient::getRequestHolderWithSign() the request params: %s" % appParams)

        if request.getBizModel():
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

        self.log.debug("DefaultAlipayClient::getRequestHolderWithSign() has the application params: %s" % requestHolder.getApplicationParams())
        
        if stringUtils.isEmpty(self.charset):
            self.charset = AlipayConstants.CHARSET_UTF8

        protocalMustParams = {}
        protocalMustParams[AlipayConstants.METHOD] = request.getApiMethodName()
        protocalMustParams[AlipayConstants.VERSION] = request.getApiVersion()
        protocalMustParams[AlipayConstants.APP_ID] = self.appId
        protocalMustParams[AlipayConstants.SIGN_TYPE] = self.sign_type
        protocalMustParams[AlipayConstants.TERMINAL_TYPE] = request.getTerminalType()
        protocalMustParams[AlipayConstants.TERMINAL_TYPE] = request.getTerminalInfo()
        protocalMustParams[AlipayConstants.NOTIFY_URL] = request.getNotifyUrl()
        protocalMustParams[AlipayConstants.RETURN_URL] = request.getReturnUrl()
        protocalMustParams[AlipayConstants.CHARSET] = self.charset

        if request.isNeedEncrypt(): # currently always return false
            protocalMustParams[AlipayContants.ENCRYPT_TYPE] = self.encryptType

        #DateFormat df = new SimpleDateFormat(AlipayConstants.DATE_TIME_FORMAT);
        #df.setTimeZone(TimeZone.getTimeZone(AlipayConstants.DATE_TIMEZONE));
        #protocalMustParams[AlipayConstants.TIMESTAMP, df.format(Datetime.datetime())]
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        protocalMustParams[AlipayConstants.TIMESTAMP] = ts
        self.log.debug("DefaultAlipayClient::getRequestHolderWithSign() going to set protocal must params: %s" % protocalMustParams)
        requestHolder.setProtocalMustParams(protocalMustParams)

        protocalOptParams = {}
        protocalOptParams[AlipayConstants.FORMAT] = self.format
        protocalOptParams[AlipayConstants.ACCESS_TOKEN] = accessToken
        protocalOptParams[AlipayConstants.ALIPAY_SDK] = AlipayConstants.SDK_VERSION
        protocalOptParams[AlipayConstants.PROD_CODE] =  request.getProdCode()
        self.log.debug("DefaultAlipayClient::getRequestHolderWithSign() going to set protocal opt params: %s" % protocalOptParams)
        requestHolder.setProtocalOptParams(protocalOptParams)

        if not stringUtils.isEmpty(self.sign_type):
            signContent = AlipaySignature.getSignatureContent(requestHolder)
            protocalMustParams[AlipayConstants.SIGN] = AlipaySignature.rsaSign(
                signContent, self.privateKey, self.charset, self.sign_type)
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
        self.log.info("DefaultAlipayClient::doPost() enter")
        requestHolder = self.getRequestHolderWithSign(request, accessToken,
                                                      appAuthToken)
        url = self.getRequestUrl(requestHolder)
        self.log.debug("doPost get the url %s" % url)
        rsp = None

        # the HTTPRequest is the thirdParty requests module, need code to monitor
        # exceptions for it
        rsp = HTTPRequest.post(url, data=requestHolder.getApplicationParams())
        #rsp = requests.post(url, data=rquestHolder.getApplicationParams(), charet,
        #                   connectTimeout, realTimeout)
        self.log.debug(rsp.content)

        result = {
            'rsp': rsp.content,
            'textParams': requestHolder.getApplicationParams(),
            'protocalMustParams': requestHolder.getProtocalMustParams(),
            'protocalOptParams': requestHolder.getProtocalOptparams(),
            'url': url
            }
        return result

    def encryptResponse(self, request, rt, parser):
        responseBody = rt.get('rsp')
        realBody = None
        if request.isNeedEncrypt():
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
        return self.serverUrl + "?" + mustQuery + "&" + optQuery
        
