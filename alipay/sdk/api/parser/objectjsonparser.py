from base_parser import AlipayParser
from jsonconverter import JsonConverter

class ObjectJsonParser(AlipayParser):
    def __init__(self, clazz):
        self.clazz = clazz

    def getResponseClass(self):
        return self.clazz

    def parser(self, rsp):
        converter = JsonConverter()
        return converter.toRsp(rsp, self.clazz)

    
        
