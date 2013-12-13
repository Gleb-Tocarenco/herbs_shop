$(document).ready(function(){
	$("#form").validate({
		rules:{
			quantity: {required: true, number: true }

		}
	});
});