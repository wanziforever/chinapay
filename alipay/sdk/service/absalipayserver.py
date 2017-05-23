import logging

class AbsAlipayService(object):
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def validateBuilder(self, builder):
        if not builder:
            raise Exception("build should not be NULL!")

        if not builder.validate():
            raise Exception("builder validate failed! " + builder.toString())

    def getResponse(self, client, request):
        try:
            response = client.execute(request)
            return response
        
        except Exception,e:
            print str(e)
            return None
