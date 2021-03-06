# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "account_tool_kit"
app_title = "Account Tool Kit"
app_publisher = "Frappe"
app_description = "account configuration for customizing the original one"
app_icon = "octicon octicon-file-directory"
app_color = "white"
app_email = "info@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/account_tool_kit/css/account_tool_kit.css"
# app_include_js = "/assets/account_tool_kit/js/account_tool_kit.js"

# include js, css files in header of web template
# web_include_css = "/assets/account_tool_kit/css/account_tool_kit.css"
# web_include_js = "/assets/account_tool_kit/js/account_tool_kit.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "account_tool_kit.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "account_tool_kit.install.before_install"
# after_install = "account_tool_kit.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "account_tool_kit.notifications.get_notification_config"

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"account_tool_kit.tasks.all"
# 	],
# 	"daily": [
# 		"account_tool_kit.tasks.daily"
# 	],
# 	"hourly": [
# 		"account_tool_kit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"account_tool_kit.tasks.weekly"
# 	]
# 	"monthly": [
# 		"account_tool_kit.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "account_tool_kit.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "account_tool_kit.event.get_events"
# }

