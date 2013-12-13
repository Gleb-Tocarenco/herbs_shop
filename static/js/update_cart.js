$(document).ready(function(){
	$("#form").on('submit', function(event){
		event.preventDefault();
		var form = $(this);
		$.ajax('some url', {
			type: 'POST',
			data: form.serialize(),
			success: function(result) {
				
			}
		});
	});
});