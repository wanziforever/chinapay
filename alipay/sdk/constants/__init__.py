# -*- coding:utf-8 -*-

class AlipayConstants:
    SIGN_TYPE = "sign_type"
    SIGN_TYPE_RSA = "RSA"

    # sha256WithRsa 算法请求类型
    SIGN_TYPE_RSA2 = "RSA2"
    sign_algorithms = "SHA1WithRSA"
    SIGN_SHA256RSA_ALGORITHMS = "SHA256WithRSA"
    ENCRYPT_TYPE_AES = "AES"
    APP_ID = "app_id"
    FORMAT = "format"
    METHOD = "method"
    TIMESTAMP = "timestamp"
    VERSION = "version"
    SIGN = "sign"
    ALIPAY_SDK = "alipay_sdk"
    ACCESS_TOKEN = "auth_token"
    APP_AUTH_TOKEN = "app_auth_token"
    TERMINAL_TYPE = "terminal_type"
    TERMINAL_INFO = "terminal_info"
    CHARSET = "charset"
    NOTIFY_URL = "notify_url"
    RETURN_URL = "return_url"
    ENCRYPT_TYPE = "encrypt_type"
    # --end--
    
    BIZ_CONTENT_KEY = "biz_content"

    # 默认时间格式
    DATE_TIME_FORMAT = "yyyy-MM-dd HH:mm:ss"

    # Date默认时区
    DATE_TIMEZONE = "GMT+8"
    
    # UTF-8字符集
    CHARSET_UTF8 = "UTF-8"

    # GBK字符集
    CHARSET_GBK = "GBK"

    # JSON应格式
    FORMAT_JSON = "json"

    # XML 应格式
    FORMAT_XML = "xml"

    # SDK版本号
    SDK_VERSION = "aliay-sdk-java-dynamicVersionNo"

    PROD_CODE = "prod_code"

    # 老版本失败节点
    ERROR_RESPONSE = "error_response"

    # 新版本节点后缀
    RESPONSE_SUFFIX = "_response"

    # 加密后XML返回报文的节点名字
    RESPONSE_XML_ENCRYPT_NODE_NAME = "response_encrypted"
    
