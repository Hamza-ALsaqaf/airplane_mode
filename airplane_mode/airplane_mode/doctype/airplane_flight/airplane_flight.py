# Copyright (c) 2024, Hamza Alsaqaf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AirplaneFlight(Document):
	def on_submit(self):
		self.db_set("status","Completed")