document.addEventListener('DOMContentLoaded', function () {
    const tdbody = document.getElementById('cohortlist');
    let isRequestInProgress = false;
    let previousCohortCount = 0; // Store the initial cohort count
    const addListUrl  = "/adminback/add_userlist"

    function CohortListfunc() {
        if (isRequestInProgress) return;  // Prevent overlapping requests
        isRequestInProgress = true;

        axios.get('/adminback/cohort_list').then(res => {
            const cohort_list = res.data.cohort_list;
            const currentCohortCount = cohort_list.length; // Get current cohort count

            // Check if the cohort count has changed
            if (currentCohortCount !== previousCohortCount) {
                tdbody.innerHTML = '';  // Clear any existing content

                cohort_list.forEach(cohorts => {
                    const trbody = document.createElement('tr');
                    let membersProfiles = '';
                    const totalMembers = cohorts.members.length;

                    cohorts.members.forEach(member => {
                        membersProfiles += `
                            <span class="avatar avatar-sm">
                                <img alt="avatar" src="/media/${member.profiles__image}" class="rounded-circle" />
                            </span>
                        `;
                    });

                    trbody.innerHTML = `
                        <td>
                            <div class="d-flex align-items-center">
                                <div class="ms-3 lh-1">
                                    <h5 class="mb-1"><a href="#!" class="text-inherit">${cohorts.name}</a></h5>
                                </div>
                            </div>
                        </td>
                        <td>
                            <div class="avatar-group">
                                ${membersProfiles}
                                <span class="avatar avatar-sm avatar-primary">
                                    <span class="avatar-initials rounded-circle fs-6">${totalMembers}</span>
                                </span>
                            </div>
                        </td>
                        <td>
                            <div class="dropdown dropstart">
                                <a class="btn btn-icon btn-ghost btn-sm rounded-circle" href="#!" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    <i class="icon-xs" data-feather="more-vertical"></i>
                                </a>
                                <div class="dropdown-menu">
                                    <a class="dropdown-item d-flex align-items-center"javascript:void(0);" onclick="deletecohort(${cohorts.id})">Delete</a>
                                     <a class="dropdown-item d-flex align-items-center" href="${addListUrl}">Add Members</a>
                            </div>
                                </div>
                            </div>
                        </td>
                    `;

                    tdbody.appendChild(trbody);
                });

                // Initialize Feather icons (if using Feather icons)
                feather.replace();

                // Update the previous cohort count to the current count
                previousCohortCount = currentCohortCount;
            }
        }).catch(error => {
            console.error('Error fetching cohort data:', error);
        }).finally(() => {
            isRequestInProgress = false;  // Reset flag when request completes
        });
    }

    // Initial data fetch
    CohortListfunc();

    // Run CohortListfunc every 3 seconds, but only refresh if the cohort list changes
    setInterval(() => {
        CohortListfunc();
    }, 1000);





    window.deletecohort = function (cohort_id) {
        axios.get(`/adminback/cohortdelete/${cohort_id}`)
            .then(res => {




                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: 'Admission Approved Successfully',
                    showConfirmButton: false,
                    timer: 1500 // 1.5 seconds

                }).then(() => {
                    fetchpending()
                    laoder.style.display = "none"

                }).then(() => {
                    // Fetch the data again to update the list
                    CohortListfunc();
                });


            }).catch(error => {
                Swal.fire({
                    position: 'top-end',
                    icon: 'error',
                    title: 'An error occurred',
                    text: 'Failed to approve the admission',
                    showConfirmButton: false,
                    timer: 20000 // 1.5 seconds
                });

            });


    }
});


