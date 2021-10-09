$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				texto : $('#texto').val(),
			},
			type : 'POST',
			url : '/'
		})
		event.preventDefault();

	});

});