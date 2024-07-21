$(window).on('load', function(){

    $('#loader').fadeIn('show', function(){
    $('#app-content').fadeIn('show');
    setInterval(function(){

        $('#loader').hide()


    },1000)


    });
})



$(document).ready(function (){
//user lout js
$('#logout').on('click', function (event) {
    console.log(event)

    event.preventDefault()
    // console.log(event)
    $('#loader').show();
    var csrftoken = $('meta[name="csrf-token"]').attr('content');
    const $message = $('#message');

    $.ajax({
        type: 'POST',
        url: '/user/logout',
        dataType: 'json',
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function (res) {
            // console.log(res)
            $message
                .removeClass('alert-danger')
                .addClass('alert-success')
                .text(res.success)

                .show();
            setTimeout(function () {
                window.location = "/user/login"

            }, 2500)

        }

    })



});



})
    