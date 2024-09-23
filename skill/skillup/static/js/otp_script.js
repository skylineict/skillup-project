$(document).ready(function () {
    $('#otp_resent').on('submit', function (event) {
        event.preventDefault();
        // console.log(event)
        const $form = $(this);
        const $btn = $('#submitbtn');
        const $spinner = $('.spinner-border');
        const $message = $('#message');
        $spinner.show();
        $btn.prop('disabled', true)
        $('#btn-text').text('Processing...');
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        // console.log(csrftoken)

        $.ajax({

            type: 'POST',
            url: '/user/resent',
            data: $form.serialize(),
            dataType: 'json',
            headers: { 'X-CSRFToken': csrftoken },

            success: function (res) {
                console.log(res)
                $message
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text(res.success)
                    .show();
                setTimeout(function () {
                    window.location = "/user/emailverify"

                }, 1000)





            },

            error: function (err) {
                // console.log(err)
                $message
                    .removeClass('alert-success')
                    .addClass('alert-danger')
                    .text(err.responseJSON.error)
                    .show();
                $spinner.hide();
                $btn.prop('disabled', false);
                $('#btn-text').text('Procced');
            }
        })
    });







});
