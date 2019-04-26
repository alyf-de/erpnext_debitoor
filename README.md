## Nextoor

[ERPNext](https://erpnext.org) App to connect with [Debitoor](https://debitoor.com).

## Install

1. Install App

```bash
  cd /home/frappe/frappe-bench
  bench get-app https://github.com/alyf-de/nextoor
  bench install-app nextoor
```

2. Get your API Key from https://developers.debitoor.com/api-console .
3. Open `Debitoor Settings` in ERPNext Desk, enter API Key and URL (https://api.debitoor.com), hit *Save*.

Now, when you submit a new `Sales Invoice` or `Purchase Invoice`, it will be synced to Debitoor.

## Known Issues

* Tax rate is fixed to the first line in table of `taxes`
* Address and note get filled with HTML instead of plain text.

## Todo

In `Debitoor Settings`

Fields:

`Check` Sync Payments from Debitoor (Daily, consider last 30 days)

Buttons:

* Export to Debitoor

  * Customers
  * Suppliers
  * Items

* Import from Debitoor

  * Customers
  * Suppliers
  * Products


#### License

Copyright (C) 2019 Raffael Meyer raffael@alyf.de

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
