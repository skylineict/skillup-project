$(document).ready(function () {
    $('#email_verify').on('submit', function (event) {
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
            url: '/user/emailverify',
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
                    window.location = "/user/profile"

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
    })
});





$(document).ready(function () {
    $('#login').on('submit', function (event) {
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
            url: '/user/login',
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



            },

            error: function (err) {
                console.log(err)
                if (err.responseJSON.verify) {
                    $message
                        .removeClass('alert-success')
                        .addClass('alert-danger')
                        .text(err.responseJSON.verify)
                        .show();
                    setTimeout(function () {
                        window.location = "/user/emailverify"

                    }, 2000)

                } if (err.responseJSON.is_profile) {
                    
                    $message
                    .removeClass('alert-success')
                    .addClass('alert-warning')
                    .text(err.responseJSON.is_profile)
                    .show();
                setTimeout(function () {
                    window.location = "/user/profile"

                }, 2000)
                }else {


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
            }
        })
    })
})




