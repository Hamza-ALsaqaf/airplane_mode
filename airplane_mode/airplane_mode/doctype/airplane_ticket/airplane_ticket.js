// Copyright (c) 2024, Hamza Alsaqaf and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
	// refresh: function(frm) {onload

	// },
	// refresh: function (frm) {
		
	// },
	update_total_amount(frm) {
		let total_d = 0
		for (let item of frm.doc.add_ons) {
			total_d += item.amount
		}
		const total_amount = total_d + frm.doc.flight_price

		frm.set_value("total_amount", total_amount)
	},
	flight_price: function(frm) {
		frm.trigger("update_total_amount");//trigger==> it will get the function and pass frm pram to it

	},
});
frappe.ui.form.on('Airplane Ticket Add-on Item', { // The child table is defined in a DoctType called "Dynamic Link"
	add_ons_add(frm, cdt, cdn) { // "links" is the name of the table field in ToDo, "_add" is the event
		
		var priviesItem = frm.doc.add_ons.map((item) => item.item);
		// console.log(priviesItem);
		frm.set_query("item", "add_ons", function () {
			let filters = {
				name: ["not in", priviesItem]
			};
			return {
				filters: filters
			};
		})
		//frm.trigger("update_total_amount");//trigger==> it will get the function and pass frm pram to it

	},
	amount:function(frm){
		frm.trigger("update_total_amount");//trigger==> it will get the function and pass frm pram to it

	},
	add_ons_remove(frm, cdt, cdn) {
		frm.trigger("update_total_amount");
	}
});
// frappe.ui.form.on('Airplane Ticket Add-on Item', {
// 	item:function()

// });
// console.log(cdt,cdn)
// console.log(frappe.get_doc(cdt,cdn));
// let my_child=frappe.get_doc(cdt, cdn)
// frappe.model.set_value(cdt, cdn,"source","Updated source");