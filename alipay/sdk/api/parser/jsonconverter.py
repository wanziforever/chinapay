
import json
from converter import Converter

class JsonConverter(Converter):
    def toRsp(self, rsp, clazz):
        rspJson = json.loads(rsp)
        rspObject = clazz()

        avpList = []
        for item in dir(rspObject):
            if item.startswith(clazz.PREFIX):
                avpList.append(item.replace(clazz.PREFIX, ''))
                
        if rspObject.getTopExpectTag() not in rspJson:
            raise Exception("no %s in response" % rspObject.getTopExpectTag())
        

        rspDetailJson = rspJson[rspObject.getTopExpectTag()]

        for avp in avpList:
            if avp in rspDetailJson:
                setattr(rspObject, clazz.PREFIX + avp, rspDetailJson[avp])

        return rspObject
