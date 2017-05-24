# -*- coding:utf-8 -*-

from base_response import AlipayResponse

class AlipayTradeQueryResponse(AlipayResponse):
    def __init__(self):
        AlipayResponse.__init__(self)
        self._ApiField_alipay_store_id = ""
        self._ApiField_buyer_logon_id = ""
        self._ApiField_buyer_pay_amount = ""
        self._ApiField_buyer_user_id = ""
        self._ApiField_discount_goods_detail = ""

        self._ApiField_fund_bill_list = []
        self._ApiField_trade_found_bill = ""
        
        self._ApiField_industry_sepc_detail = ""
        self._ApiField_invoice_amount = ""
        self._ApiField_open_id = ""
        self._ApiField_out_trade_no = ""
        self._ApiField_point_amount = ""
        self._ApiField_receipt_amount = ""
        self._ApiField_send_pay_date = ""
        self._ApiField_store_id = ""
        self._ApiField_store_name = ""
        self._ApiField_terminal_id = ""
        self._ApiField_total_amount = ""
        self._ApiField_trade_no = ""
        self._ApiField_trade_status = ""
        self._ApiField_voucher_detail_list = []
        self._ApiField_voucher_detail = ""

    def getTopExpectTag(self):
        return 'alipay_trade_query_response'

        # following are getters
