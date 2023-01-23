from __future__ import unicode_literals
from . import __version__ as app_version
from . import __logo__ as app_logo


app_name = "branding"
app_title = "Branding"
app_publisher = "Novacept"
app_description = "Branding for the Toolkit"
app_email = "info@novacept.io"
app_license = "MIT"
app_logo_url = '/assets/branding/images/sample.jpg'


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/branding/css/novacept.css"
web_include_css = "/assets/branding/css/login.css"

app_include_js = "/assets/branding/js/novacept.js"

# include js, css files in header of web template
# web_include_css = "/assets/branding/css/login.css"
# web_include_js = "/assets/branding/js/branding.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "branding/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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
website_context = {
	"favicon": app_logo or "/branding/public/images/sample.jpg",
	"splash_image": app_logo or "/branding/public/images/sample.jpg"
}
after_migrate = ['whitelabel.api.whitelabel_patch']

#system wizard 


# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "branding.utils.jinja_methods",
#	"filters": "branding.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "branding.install.before_install"
# after_install = "branding.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "branding.uninstall.before_uninstall"
# after_uninstall = "branding.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "branding.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"branding.tasks.all"
#	],
#	"daily": [
#		"branding.tasks.daily"
#	],
#	"hourly": [
#		"branding.tasks.hourly"
#	],
#	"weekly": [
#		"branding.tasks.weekly"
#	],
#	"monthly": [
#		"branding.tasks.monthly"
#	],
# }

boot_session = "branding.api.boot_session"


# Testing
# -------

# before_tests = "branding.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "branding.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "branding.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"branding.auth.validate"
# ]

override_whitelisted_methods = {
	"frappe.utils.change_log.show_update_popup": "branding.api.ignore_update_popup"
}