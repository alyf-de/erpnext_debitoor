from nextoor.nextoor.api import post

def sales_invoice_on_submit(sinv, event):
	""" Construct Sales Invoice payload and post to Debitoor """
	payload = get_sales_invoice_payload(sinv)
	post('/api/sales/draftinvoices/v3', payload)

def purchase_invoice_on_submit(pinv, event):
	""" Construct Purchase Invoice payload and post to Debitoor """
	payload = get_purchase_invoice_payload(pinv)
	post('/api/expenses/v4', payload)

def get_sales_invoice_payload(sinv):
    payload = {
            'number': sinv.name,
            'date': sinv.posting_date, #.isoformat(),
            'dueDate': sinv.due_date, #.isoformat(),
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
    return payload


def get_purchase_invoice_payload(pinv):
    payload = {
            'number': pinv.name,
            'date': pinv.posting_date, #.isoformat(),
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

    return payload
