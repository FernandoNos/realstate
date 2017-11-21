$(document).ready(function() {
    $.ajax({
        url: "http://127.0.0.1:5000/updateRealties"
    }).then(function(data) {
       $('.greeting-id').append(data);
       $('.greeting-content').append(data);
    });
});