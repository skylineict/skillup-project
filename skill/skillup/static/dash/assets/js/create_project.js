document.addEventListener('DOMContentLoaded', function () {
    const projectform = $('#projectform')
    const btntext = $('#btntext')
    const spinner = $('#spinner')
    const projectbtn = $('#projectbtn')







    $(projectform).on('submit', function (e) {
        e.preventDefault();
        const $form = $(this);
        projectbtn.prop('disabled', true);
        spinner.show()
        console.log($form)
        btntext.text('creating..')


        var csrftoken = $("[name=csrfmiddlewaretoken]").val();


        $.ajax({
            type: 'POST',
            url: '/adminback/add_project',
            data: $form.serialize(),
            dataType: 'json',
            headers: { 'X-CSRFToken': csrftoken },
            success: function (res) {
                console.log(res)
           
                projectbtn.prop('disabled', true);
                spinner.hide()
                btntext.text('Creating..')
                iziToast.success({
                    title: 'Success',
                    message: res.success,
                    position: 'topRight'
                });

             
                // $form.trigger('reset');
       



            },

            error: function (err) {
                projectbtn.prop('disabled', false);
                spinner.hide()
                btntext.text('Create Project')
                console.log(err.responseJSON.error)
                iziToast.error({
                    title: 'Error',
                    message: err.responseJSON.error,
                    position: 'topRight'
                });


               


            }





        });













    });


})