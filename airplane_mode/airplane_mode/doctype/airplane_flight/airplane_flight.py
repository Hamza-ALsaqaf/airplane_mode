# Copyright (c) 2024, Hamza Alsaqaf and contributors
# For license information, please see license.txt

import frappe
# from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import time_diff_in_hours, formatdate,format_duration
class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.db_set("status","Completed")
	# @frappe.whitelist()
	def durationFormat(self):
		# return "01:12"
		return format_duration(self.duration,True)
