# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "nextoor"
app_title = "Nextoor"
app_publisher = "Raffael Meyer"
app_description = "ERPNext App to connect with Debitoor"
app_icon = "octicon octicon-repo-pull"
app_color = "#1eb5ff"
app_email = "nextoor@alyf.de"
app_license = "GPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nextoor/css/nextoor.css"
# app_include_js = "/assets/nextoor/js/nextoor.js"

# include js, css files in header of web template
# web_include_css = "/assets/nextoor/css/nextoor.css"
# web_include_js = "/assets/nextoor/js/nextoor.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "nextoor.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nextoor.install.before_install"
# after_install = "nextoor.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nextoor.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Sales Invoice" : {
		"on_submit": "nextoor.nextoor.hooks.sales_invoice_on_submit"
	},
	"Purchase Invoice" : {
		"on_submit": "nextoor.nextoor.hooks.purchase_invoice_on_submit"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nextoor.tasks.all"
# 	],
# 	"daily": [
# 		"nextoor.tasks.daily"
# 	],
# 	"hourly": [
# 		"nextoor.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nextoor.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nextoor.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "nextoor.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nextoor.event.get_events"
# }

