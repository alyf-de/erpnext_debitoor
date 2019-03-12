## Nextoor

[ERPNext](erpnext.org) App to connect with [Debitoor](debitoor.com).

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

#### License

GPL
