import json
import base64
import textwrap
import logging
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256, SHA
from Crypto.PublicKey import RSA

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

log = logging.getLogger("AlipaySignature")

class AlipaySignature(object):
    @staticmethod
    def getSignatureContent(requestHolder):
        allParams = {}
        appParams = requestHolder.getApplicationParams()
        allParams.update(appParams)
        protocalMustParams = requestHolder.getProtocalMustParams()
        allParams.update(protocalMustParams)
        protocalOptParams = requestHolder.getProtocalOptParams()
        allParams.update(protocalOptParams)
        return AlipaySignature.serialize_map(allParams)

    @staticmethod
    def serialize_map(dictData):
        def orderedData(dictData):
            complexKeys = []
            for key, value in dictData.items():
                if isinstance(value, dict):
                    complexKeys.append(key)
            for key in complexKeys:
                dictData[key] = json.dumps(dictData[key], sort_keys=True,
                                       ensure_ascii=False).replace(" ", "")
            return sorted([(k, v) for k, v in dictData.items()])
        

        #targetString = '&'.join("{}={}".format(k, v) \
        #                        for k, v in items if len(v)!=0)
        items = []
        for k, v in orderedData(dictData):
            if v is None or len(v.strip()) == 0:
                continue
            items.append((k, v))

        targetString = '&'.join("{}={}".format(k, v) for k, v in items )
        return targetString

    @staticmethod
    def rsaSign(signContent, privateKey, charset, signType):
        private_string = "-----BEGIN RSA PRIVATE KEY-----\n"
        private_string += textwrap.fill(privateKey, 64)
        private_string += "\n-----END RSA PRIVATE KEY-----\n"
        key = RSA.importKey(private_string)
        signer = PKCS1_v1_5.new(key)
        log.debug("AlipaySignature.rsaSign with RSA2 algorithm")
        if signType.upper() == "RSA2":
            signature = signer.sign(SHA256.new(signContent.encode("utf8")))
        elif signType.upper() == "RSA":
            signature = signer.sign(SHA.new(signContent.encode("utf8")))
        else:
            raise Exception("unsupport signType %s, currently only support RSA or RSA2 " % signType)
        return base64.b64encode(signature).decode("utf8")
