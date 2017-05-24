from base_parser import AlipayParser
from jsonconverter import JsonConverter

class ObjectJsonParser(AlipayParser):
    def __init__(self, clazz):
        AlipayParser.__init__(self)
        self.clazz = clazz

    def getResponseClass(self):
        return self.clazz

    def parse(self, rsp):
        converter = JsonConverter()
        return converter.toRsp(rsp, self.clazz)

    
        
