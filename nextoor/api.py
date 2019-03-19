import requests
import json

import frappe
from frappe import msgprint


def sales_invoice_on_submit(sinv):
	""" Construct Sales Invoice payload and post to Debitoor """
	payload = {
		'number': sinv.name,
		'date': sinv.posting_date.isoformat(),
		'dueDate': sinv.due_date.isoformat(),
		'notes': sinv.terms,
		'additionalNotes': "",
		'customerName': sinv.customer,
		'customerAddress': sinv.address_display,
		'customerVatNumber': sinv.tax_id,
		'paymentTermsId': 3,
		'lines': [],
		'discountRate': sinv.additional_discount_percentage,
		'currency': sinv.currency,
	}

	for item in sinv.items:
		payload['lines'].append({
			'productName': item.item_name,
			'quantity': item.qty,
			'unitNetPrice': item.rate,
			'description': item.description,
			'taxEnabled': True,
			'taxRate': pinv.taxes[0].rate
		})

	post('/api/sales/draftinvoices/v3', payload)


def purchase_invoice_on_submit(pinv):
	""" Construct Purchase Invoice payload and post to Debitoor """
	payload = {
		'number': pinv.name,
		'date': pinv.posting_date.isoformat(),
		'supplierName': pinv.supplier,
		'supplierAddress': pinv.address_display,
		'supplierCiNumber': pinv.tax_id,
		'lines': []
	}

	for item in pinv.items:
		payload['lines'].append({
			'netAmount': item.amount,
			'description': item.description,
			'taxRate': pinv.taxes[0].rate
		})

	post('/api/expenses/v4', payload)


def post(endpoint, payload):
	""" Get credentials and post payload to Debitoor endpoint """
	config = frappe.get_doc('Debitoor Settings')

	if not (config.url and config.api_key):
		return

	headers = {
		'content-type': 'application/json',
		'Authorization': 'Bearer ' + config.api_key
	}

	r = requests.post(config.url + endpoint,
					  data=json.dumps(payload), headers=headers)
	if r.raise_for_status():
		msgprint(r.text)


def test():
	""" 
	Helper to quickly test on live-system 
	
	~/frappe-bench$ bench console
	In [1]:  from nextoor.api import test
	In [2]:  test()
	"""
	first_sinv = frappe.get_list('Sales Invoice')[0].name
	sinv = frappe.get_doc('Sales Invoice', first_sinv)
	sales_invoice_on_submit(sinv)
