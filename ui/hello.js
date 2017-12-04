$(document).ready(function() {
    $.ajax({
    	data:{page:'1'},
        url: "http://127.0.0.1:8000/updateRealties"
    }).then(function(data) {
       $('.greeting-id').append(data);
       $('.greeting-content').append(data);
    });
});