import unittest

from nextoor.nextoor.hooks import get_purchase_invoice_payload
from nextoor.nextoor.hooks import get_sales_invoice_payload


class TestStringMethods(unittest.TestCase):

    def test_get_purchase_invoice_payload(self):
        items = {
            'name': 'PINV-0001',
            'posting_date': '2019-02-28',
            'supplier': 'Muster GmbH',
            'address_display': '',
            'tax_id': '123456',
            'taxes': [
                {
                    'rate': 19
                }
            ],
            'items': [
                {
                    'amount': 100,
                    'description': ''
                }
            ]
        }

        get_purchase_invoice_payload(pinv, 'on_sumit')

    def test_get_sales_invoice_payload(self):
        sinv = {
            'name': 'SINV-0001',
            'posting_date': '2019-02-28',
            'due_date': '2019-03-14',
            'terms': '',
            'customer': 'Muster GmbH',
            'address_display': '',
            'tax_id': '123456',
            'items': [
                {
                    'item_name': '',
                    'qty': 1,
                    'rate': 100,
                    'description': ''
                }
            ],
            'taxes': [
                {
                    'rate': 19
                }
            ],
            'additional_discount_percentage': 10,
            'currency': 'EUR'
        }

        get_sales_invoice_payload(sinv, 'on_submit')


if __name__ == '__main__':
    unittest.main()
