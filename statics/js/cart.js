$(function(){

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $("#purchase").on("click", function(){
        var cart_id = $("table").attr('id');

        $.post("/carts/purchase/", 
            { 'cart_id': cart_id },
            function(data){
                window.location.reload();
                alert("Purchase is successful!");
            }
        );
    });

    $(".delete").on("click", function(){
        var cart_id = $("table").attr('id');
        var cart_item_id = $(this).attr('id');
    
        $.post("/carts/delete/", 
            { 'cart_id': cart_id, 'cart_item_id': cart_item_id },
            function(data){
                // console.log(data);
                window.location.reload();
            }
        );
    });

});