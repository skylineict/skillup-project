
$(document).ready(function () {
    $('#register').on('submit', function (event) {
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
            url: '/user/',
            data: $form.serialize(),
            dataType: 'json',
            headers: { 'X-CSRFToken': csrftoken },

            success: function (res) {
                // console.log(res.success)
                $message
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text(res.success)

                    .show();
                setTimeout(function () {
                    window.location = "/user/emailverify"

                }, 2000)




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
                $('#btn-text').text('Sign Up');
            }
        })
    })
})


const departmentDiv = document.getElementById('department');
const facultySelect = document.getElementById('faculty');
const level = document.getElementById('level')

facultySelect.addEventListener('change', function () {


    if (facultySelect.value !== 'choose') {
        departmentDiv.style.display = 'block';
        level.style.display = 'block';
    } else {
        console.log('Hiding department field');
        departmentDiv.style.display = 'none';
        level.style.display = 'none';
    }
});

//profile start from here 

$(document).ready(function () {
    $('#profile').on('submit', function (event) {
        event.preventDefault();
        // console.log(event)
        const $form = $(this);
        const $btn = $('#submitbtn');
        const $spinner = $('.spinner-border');
        const $message = $('#message');
        $spinner.show();
        $btn.prop('disabled', true)
        $('#btn-text').text('updating.....');
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        // console.log(csrftoken)

        $.ajax({

            type: 'POST',
            url: '/user/profile',
            data: $form.serialize(),
            dataType: 'json',
            headers: { 'X-CSRFToken': csrftoken },

            success: function (res) {
                // console.log(res.success)
                $message
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text(res.success)

                    .show();
                setTimeout(function () {
                    window.location = "/user/emailverify"

                }, 2000)
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
                $('#btn-text').text('Sign Up');
            }
        })
    })
})



const  login = document.getElementById('logout')
console.log(login)