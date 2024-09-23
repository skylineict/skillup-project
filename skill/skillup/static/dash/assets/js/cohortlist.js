document.addEventListener('DOMContentLoaded', function () {
    const cohortsubmit = $('#cohortsubmit')
    const btntext = $('#btn-text')
    const spinner = $('#spinner')
    const cohortName = $('#cohortName')
    const cohortLink = $('#cohortLink')
    const createcohort = $('#createcohort')




    $('#cohortform').on('submit', function (e) {
        e.preventDefault();
        const $form = $(this);
        cohortsubmit.prop('disabled', true);
        spinner.show()
        // cohortLink.prop('disabled', true);
        // cohortName.prop('disabled', true);
        // $('#cohortform :input').prop('disabled', true);
        btntext.text('saving...')


        var csrftoken = $("[name=csrfmiddlewaretoken]").val();


        $.ajax({
            type: 'POST',
            url: '/adminback/createcohort',
            data: $form.serialize(),
            dataType: 'json',
            headers: { 'X-CSRFToken': csrftoken },
            success: function (res) {
                console.log(res)
                Swal.fire({

                    text: res.success,
                    icon: 'success', // Error icon
                    showClass: {
                        popup: `
                        animate__animated
                        animate__fadeInUp
                        animate__faster
                      `
                    },
                    hideClass: {
                        popup: `
                        animate__animated
                        animate__fadeOutDown
                        animate__faster
                      `
                    }
                });
                cohortsubmit.prop('disabled', false);
                spinner.hide()
                cohortLink.prop('disabled', false);
                cohortName.prop('disabled', false);
                btntext.text('save')
                $form.trigger('reset');
                createcohort.modal('hide');




            },

            error: function (err) {
                cohortsubmit.prop('disabled', false);
                spinner.hide()
                cohortLink.prop('disabled', false);
                cohortName.prop('disabled', false);
                btntext.text('save')

                Swal.fire({

                    text: err.responseJSON.error,
                    icon: 'error', // Error icon
                    showClass: {
                        popup: `
                        animate__animated
                        animate__fadeInUp
                        animate__faster
                      `
                    },
                    hideClass: {
                        popup: `
                        animate__animated
                        animate__fadeOutDown
                        animate__faster
                      `
                    }
                });


            }





        });













    });


})