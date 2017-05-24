from result import Result
from sdk.model.tradestatus import TradeStatus

class AlipayF2FQueryResult(Result):
    def __init__(self, response):
        self.tradeStatus = None
        self.response = response

    def setTradeStatus(self, tradeStatus):
        self.tradeStatus = tradeStatus

    def getTradeStatus(self):
        return self.tradeStatus

    def setResponse(self, response):
        self.response = response

    def getResponse(self):
        return self.response

    def isTradeSuccess(self):
        return response is not None and \
               TradeStatus.SUCCESS == self.tradeStatus
        
