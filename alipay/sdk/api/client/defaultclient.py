from base_client import AlipayClient
from sdk.constants import AlipayConstants
from sdk.api.request.requestparametersholder import RequestParameterHolder
from sdk.api.parser import ObjectJsonParser
from sdk.api.response.responseencryptitem import ResponseEncryptItem
import requests

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
        
        for arg in args:
            avp = internals.pop(1)
            setattr(self, avp, arg)

        #print "following avps not initialized", ",".join(internals)

    def getRequestHolderWithSign(self, request, accessToken, appAuthToken):
        requestHolder = RequestParameterHolder()
        appParams = request.getTextParams()
        appParams[AlipayConstants.BIZ_CONTENT_KEY, request.getBizModel()]
        if request.isNeedEncrypt():
            AlipayEncrypt.encryptContent(
                appParams.get(AlipayConstrants.BIZ_CONTENT_KEY),
                self.encryptType, self.encryptkey, self.charset)

        if not stringUtils.isEmpty(appAuthToken):
            appParams.put(AlipayConstants.APP_AUTH_TOKEN, appAuthToken)

        requestHolder.setApplicationParams(appParams)

        if stringUtils.isEmpty(charset):
            charset = AlipayContants.CHARSET_UTF8

        protocalMustParams = {}
        protocalMustParams[AlipayContants.METHOD] = request.getApiMethodName()
        protocalMustParams[AlipayContants.VERSION] = request.getApiVersion()
        protocalMustParams[AlipayContants.APP_ID] = self.appId
        protocalMustParams[AlipayContants.SIGN_TYPE] = self.sign_type
        protocalMustParams[AlipayContants.TERMINAL_TYPE] = request.getTerminalType()
        protocalMustParams[AlipayContants.TERMINAL_TYPE] = request.getTerminalInfo()
        protocalMustParams[AlipayContants.NOTIFY_URL] = request.getNotifyUrl()
        protocalMustParams[AlipayContants.RETURN_URL] = request.getReturnUrl()
        protocalMustParams[AlipayContants.CHARSET] = charset
        
        if request.isNeedEncrypt():
            protocalMustParams[AlipayContants.ENCRYPT_TYPE] = self.encryptType

        timestamp = int(time.time() * 1000)
        #DateFormat df = new SimpleDateFormat(AlipayConstants.DATE_TIME_FORMAT);
        #df.setTimeZone(TimeZone.getTimeZone(AlipayConstants.DATE_TIMEZONE));
        protocalMustParams[AlipayConstants.TIMESTAMP, df.format(Datetime.datetime())]
        requestHolder.setProtocalMustParams(protocalMustParams)

        protocalOptParams = {}
        protocalOptParams[AlipayConstants.FORMAT] = format
        protocalOptParams[AlipayConstants.ACCESS_TOKEN] = accessToken
        protocalOptParams[AlipayConstants.ALIPAY_SDK] = AlipayConstants.SDK_VERSION
        protocalOptParams[AlipayConstants.PROD_CODE] =  request.getProdCode()
        requestHolder.setProtocalOptParams(protocalOptParams)

        if stringUtils.isEmpty(self.sign_type):
            signContent = AlipaySignature.getSignatureContent(requestHolder)
            protocalMustParams[AlipayConstants.SIGN] = AlipaySignature.rsaSign(
                signContent, privateKey, charset, self.sign_type)
        else:
            protocalMustParams[AlipayContants.SIGN] = ""

        return requestHolder
      
    def execute(self, request, authToken=None, appAuthToken=None):
        self.log.info("execute going to do execute")

        # currently only support json format response, so do not need to check
        # the format property. if futher format like XML, will add a XML parser
        parser = ObjectJsonParser()
        
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
        self.log.info("doPost enter")
        requestHolder = self.getRequestHolderWithSign(request, accessToken,
                                                      appAuthToken)
        url = getRequestUrl(requestHolder)
        self.log.debug("doPost get the url %s" % url)
        rsp = None

        rsp = requests.post(url, data=rquestHolder.getApplicationParams())
        #rsp = requests.post(url, data=rquestHolder.getApplicationParams(), charet,
        #                   connectTimeout, realTimeout)

        result = {
            'rsp': rsp.content,
            'textParams': requestHolder.getApplicationparams(),
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
