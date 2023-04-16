frappe.ready(function() {
	// bind events here
	frappe.web_form.after_load=()=>{
		var grid=frappe.web_form.fields_dict['feedback'].grid;
		for( var i=0;i<5;i++){
			var row=grid.add_new_row(i);
		};
		console.log(grid,row,"----------------------");
		var grid1=frappe.web_form.fields_dict['goal'].grid;
		for( var i=0;i<2;i++){
			var row=grid1.add_new_row(i);
		};
	};
})
