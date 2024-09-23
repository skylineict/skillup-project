document.addEventListener('DOMContentLoaded', function () {
  const tbody = document.getElementById('add-student')
  const coursehtml = document.getElementById('selectcourseid')
  const usersearch = document.getElementById('search-input')
  const cohortSelect = document.getElementById('selectcohortid');
  const addToCohortBtn = document.getElementById('add-to-cohort-btn');
  let selectedstudentid = '';
  let query = '';




  function dateformate(datedatas) {
    const deteoption = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
    const date = new Date(datedatas)
    return date.toLocaleString(undefined, deteoption)


  }

  function courseList() {
    axios.get('/adminback/listcourse').then(res => {
      const courselists = res.data.list_courses
      coursehtml.innerHTML = '<option value=""selected>Choose a course</option>';


      courselists.forEach(listcourse => {
        const options = document.createElement('option');
        options.value = listcourse.id
        options.textContent = listcourse.name
        coursehtml.appendChild(options)

      });





    });

  };



  function CohortList() {
    axios.get('/adminback/list_cohort').then(res => {
      const cohorts = res.data.cohort_list
      cohortSelect.innerHTML = '<option value=""selected>select cohort</option>';
      cohorts.forEach(cohort => {
        const options = document.createElement('option');
        options.value = cohort.id;
        options.textContent = cohort.name
        cohortSelect.appendChild(options)


      });


    })

  }


  CohortList()





  function ListStudents() {
    axios.get('/adminback/addapi').then(res => {
      const list_student = res.data.admitted_list
      // console.log(res)

      tbody.innerHTML = '';

      list_student.forEach(studentdata => {
        const tbodydata = document.createElement('tr')

        tbodydata.innerHTML = `

            <td class="pe-0">
                        <div class="form-check">
                          <input class="form-check-input student-checkbox" type="checkbox" value="${studentdata.id}" id="contactCheckbox2">
                          <label class="form-check-label" for="contactCheckbox2">
                          </label>
                        </div>
                      </td>
                      <td class="ps-0">
                        <a href="#!">${studentdata.id}</a>
                      </td>

                      <td class="ps-1">
                        <div class="d-flex align-items-center">
                          <a href="#!"><img src="/media/${studentdata.profiles__image}" alt="Image"
                              class="avatar avatar-sm rounded-circle"></a>
                          <div class="ms-2">
                            <h5 class="mb-0"> <a href="#!" class="text-inherit">${studentdata.full_name}</a></h5>
                          </div>
                        </div>
                      </td>
                      <td>${studentdata.profiles__course__name}</td>

                      <td>${studentdata.email}</td>
                      <td>${dateformate(studentdata.profiles__date)}</td>
                      <td>
                        <span class="badge badge-warning-soft text-warning">${studentdata.profiles__department}</span>
                      </td> `;

        tbody.appendChild(tbodydata)

      })

    })

      .catch(error => {
        console.log('failed')


      })



  }





  function fillteredStudent(course_id) {
    axios.get('/adminback/fitterbycourse', { params: { course_id: course_id } })
      .then(res => {

        const list_student = res.data.student_list
        // console.log(res)

        tbody.innerHTML = '';

        if (list_student.length === 0) {
          const nodatatable = document.createElement('tr');
          nodatatable.innerHTML = '<td colspan="7" class="text-center"> student Not found</td>';
          tbody.appendChild(nodatatable)


        }

        list_student.forEach(studentdata => {
          const tbodydata = document.createElement('tr')

          tbodydata.innerHTML = `

           <td class="pe-0">
                        <div class="form-check">
                          <input class="form-check-input student-checkbox" type="checkbox" value="${studentdata.id}" id="contactCheckbox2">
                          <label class="form-check-label" for="contactCheckbox2">
                          </label>
                        </div>
                      </td>
                      <td class="ps-0">
                        <a href="#!">${studentdata.id}</a>
                      </td>

                      <td class="ps-1">
                        <div class="d-flex align-items-center">
                          <a href="#!"><img src="/media/${studentdata.profiles__image}" alt="Image"
                              class="avatar avatar-sm rounded-circle"></a>
                          <div class="ms-2">
                            <h5 class="mb-0"> <a href="#!" class="text-inherit">${studentdata.full_name}</a></h5>
                          </div>
                        </div>
                      </td>
                      <td>${studentdata.profiles__course__name}</td>

                      <td>${studentdata.email}</td>
                      <td>${dateformate(studentdata.profiles__date)}</td>
                      <td>
                        <span class="badge badge-warning-soft text-warning">${studentdata.profiles__department}</span>
                      </td> `;

          tbody.appendChild(tbodydata)

        })

      })

      .catch(error => {
        console.log('failed')


      });



  }

  coursehtml.addEventListener('change', function () {
    selectedstudentid = this.value;
    if (selectedstudentid) {
      fillteredStudent(selectedstudentid)

    } else {
      ListStudents();

    }

  })




  function searchStudent(query) {
    axios.get('/adminback/usersearch', { params: { query: query } })
      .then(res => {
        // console.log(res)

        const list_student = res.data.student_list
        // console.log(res)

        tbody.innerHTML = '';

        if (list_student.length === 0) {
          const nodatatable = document.createElement('tr');
          nodatatable.innerHTML = '<td colspan="7" class="text-center"> student Not found</td>';
          tbody.appendChild(nodatatable)


        }

        list_student.forEach(studentdata => {
          const tbodydata = document.createElement('tr')

          tbodydata.innerHTML = `

             <td class="pe-0">
                        <div class="form-check">
                          <input class="form-check-input student-checkbox" type="checkbox" value="${studentdata.id}" id="contactCheckbox2">
                          <label class="form-check-label" for="contactCheckbox2">
                          </label>
                        </div>
                      </td>
                      <td class="ps-0">
                        <a href="#!">${studentdata.id}</a>
                      </td>

                      <td class="ps-1">
                        <div class="d-flex align-items-center">
                          <a href="#!"><img src="/media/${studentdata.profiles__image}" alt="Image"
                              class="avatar avatar-sm rounded-circle"></a>
                          <div class="ms-2">
                            <h5 class="mb-0"> <a href="#!" class="text-inherit">${studentdata.full_name}</a></h5>
                          </div>
                        </div>
                      </td>
                      <td>${studentdata.profiles__course__name}</td>

                      <td>${studentdata.email}</td>
                      <td>${dateformate(studentdata.profiles__date)}</td>
                      <td>
                        <span class="badge badge-warning-soft text-warning">${studentdata.profiles__department}</span>
                      </td> `;

          tbody.appendChild(tbodydata)

        })

      })

      .catch(error => {
        console.log('failed')


      });



  }

  usersearch.addEventListener('input', function () {

    query = usersearch.value.trim();
    if (query.length >= 3) {
      searchStudent(query)


    } else {
      ListStudents();

    }
  })






  addToCohortBtn.addEventListener('click', function () {

    const selectedCheckboxes = document.querySelectorAll('.student-checkbox:checked');
    const studentid = []
    selectedCheckboxes.forEach(student_id => {
      studentid.push(student_id.value)

    });
    // console.log(studentid)
    const cohortid = cohortSelect.value
    if (studentid.length > 0 && cohortid) {
      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;



      axios.post('/adminback/add_user_cohort', { student_ids: studentid, cohort_id: cohortid }, {

        headers: {
          'X-CSRFToken': csrfToken
        }
      })
        .then(res => {



          Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: res.data.success,
            showConfirmButton: false,
            timer: 1500 // 1.5 seconds

          })

        })

        .catch(error => {
          const errorData = error.response.data;

          Swal.fire({
            position: 'top-end',
            icon: 'error',
            text: errorData.error,
            showConfirmButton: false,
            timer: 20000// 1.5 seconds
          });

        })

    }
    // console.log('here is my cohort id', cohortid)


  })



  courseList();
  ListStudents();


  setInterval(() => {
    if (!selectedstudentid && !query) {
      ListStudents();
    }

  }, 30000);





})


