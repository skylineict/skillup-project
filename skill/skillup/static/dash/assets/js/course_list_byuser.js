document.addEventListener('DOMContentLoaded', function() {
    // Check if the tbody container exists
    const tbody_container = document.getElementById('Course_list_Bycateogry');
   

    // Define the function to list students by course ID
    function ListStudent_by(course_id) {
        axios.get(`/adminback/user_courselist/${course_id}`)
            .then(res => {
                const studentdata = res.data.student_list;
                console.log('Data received:', studentdata);

                tbody_container.innerHTML = '';

                if (studentdata.length === 0) {
                    const nodatatable = document.createElement('tr');
                    nodatatable.innerHTML = '<td colspan="7" class="text-center">Student Not Found</td>';
                    tbody_container.appendChild(nodatatable);
                } else {
                    studentdata.forEach(students => {
                        const tbodydatas = document.createElement('tr');
                        tbodydatas.innerHTML = `
                            <td>
                                <div class="d-flex align-items-center">
                                    <div class="ms-3 lh-1">
                                        <h5 class="mb-1"><a href="#!" class="text-inherit">${students.user__full_name}</a></h5>
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div class="d-flex align-items-center">
                                    <div class="ms-3 lh-1">
                                        <h5 class="mb-1"><a href="#!" class="text-inherit">${students.course__name}</a></h5>
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div class="d-flex align-items-center">
                                    <div class="ms-3 lh-1">
                                        <h5 class="mb-1"><a href="#!" class="text-inherit">${students.user__email}</a></h5>
                                    </div>
                                </div>
                            </td>
                        `;
                        tbody_container.appendChild(tbodydatas);
                    });
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    const courseId = document.getElementById('courseId').value;
    ListStudent_by(courseId);



    
});
