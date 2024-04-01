# Copyright (c) 2024, Hamza Alsaqaf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string
# from frappe.utils import unique
class AirplaneTicket(Document):
	def before_save(self):
		pass
	def validate(self):
		self.remove_duplicate_add_ons_item()

	def remove_duplicate_add_ons_item(self):
		# Check for duplicate entries and remove them
		seen = set()
		duplicates = []

		for entry in self.add_ons:
			key = (entry.item)
			if key in seen:
				duplicates.append(entry)
			else:
				seen.add(key)

		# Remove duplicates from the document
		for duplicate in duplicates:
			self.add_ons.remove(duplicate)

	def before_submit(self):
		if self.doctype == "Airplane Ticket" and self.status != "Boarded":
			frappe.throw("Airplane Ticket can only be submitted if the status is 'Boarded'.")

	def generate_random_seat(self):
		# Generate a random integer between 10 and 99
		random_integer = random.randint(10, 99)
		# Generate a random capital alphabet from A to E
		random_alphabet = random.choice(string.ascii_uppercase[:5])
		seat_number = f"{random_integer}{random_alphabet}"
		return seat_number
	def before_insert(self):
		if self.is_new():
			seat_number = self.generate_random_seat()
			# frappe.errprint(seat_number)
			self.seat = seat_number