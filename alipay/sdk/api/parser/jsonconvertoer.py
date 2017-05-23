from converter import Converter

class JsonConverter(Converter):
    def toResponse(self, rsp, clazz):
        return clazz()
