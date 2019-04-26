import requests
import json

import frappe
from frappe import msgprint


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
	In [1]:  from nextoor.nextoor.api import test
	In [2]:  test()
	"""
	first_sinv = frappe.get_list('Sales Invoice')[0].name
	sinv = frappe.get_doc('Sales Invoice', first_sinv)
	sales_invoice_on_submit(sinv)
