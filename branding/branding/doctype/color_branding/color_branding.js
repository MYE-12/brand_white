// Copyright (c) 2023, Novacept and contributors
// For license information, please see license.txt

frappe.ui.form.on('Color Branding', {
	// refresh: function(frm) {

	// }
	after_save: function(frm) {
		frappe.ui.toolbar.clear_cache();
	}
});
