$(document).ready(function(){
	$(".button_plus").on("click", function(){
		var inputField = $(this).parent().parent().find("input").first();
		var sub_total = $(this).closest(".table_data").find("td").last();
		var cart_total = $("#cart_total");


		var oldValue = +inputField.val();
		var newValue = oldValue + 1;
		var sub_total_new = +inputField.data("price") * newValue;
		var cart_total_new = +cart_total.text() - +sub_total.text() + sub_total_new;

		inputField.val(newValue);
		cart_total.text(cart_total_new);
		sub_total.text(sub_total_new);
		
		
	});

	$(".button_minus").on("click", function(){
		var inputField = $(this).parent().parent().find("input").first();
		var oldValue = +inputField.val();
		var newValue = oldValue - 1;

		var sub_total = $(this).closest(".table_data").find("td").last();
		var cart_total = $("#cart_total");

		if (newValue <  0) {
			inputField.val(0);
			newValue = 0;
		} else {
			inputField.val(newValue);
		}
		var sub_total_new = +inputField.data("price") * newValue;
		var cart_total_new = +cart_total.text() - +sub_total.text() + sub_total_new;

		cart_total.text(cart_total_new);
		sub_total.text(sub_total_new);
	});
});