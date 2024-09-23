

document.addEventListener('DOMContentLoaded', function () {
    const tbody = document.getElementById('pending-admissions-body');
    const prevsbtn = document.getElementById('prev-page');
    const nextpagebtn = document.getElementById('next-page');
    let currentpage = 1;
    let totalpages = 1;

    // admissionapproved()
    // console.log(tbody)
    function fetchpending(page = 1) {
        axios.get(`/adminback/pending_admission?page=${page}`)
            .then(res => {
                console.log(res)
                tbody.innerHTML = '';
                res.data.profiles.forEach(profile => {
                    const tr = document.createElement('tr')
                    // console.log(profile)
                    const date = new Date(profile.date)
                    // console.log(date.getFullYear())
                    tr.innerHTML = `
              
														<td>
															<div class="d-flex align-items-center">
																<div>
																	<a href="#!"><img src="/media/${profile.image}" alt="Image" class="avatar-md avatar rounded-circle" /></a>
																</div>
																<div class="ms-3 lh-1">
																	<h5 class="mb-1"><a href="#!" class="text-inherit">${profile.user__full_name}</a></h5>
																
																</div>
															</div>
														</td>
                                                         <td> ${profile.user__email}</td>
                                                         <td> ${profile.course__name}</td>
														<td>${profile.department}</td>
														<td> ${profile.user__email}</td>
                                                       
														<td>
															<div class="dropdown dropstart">
																<a
																	class="btn btn-icon btn-ghost btn-sm rounded-circle"
																	href="#!"
																	role="button"
																	id="dropdownTeamOne"
																	data-bs-toggle="dropdown"
																	aria-haspopup="true"
																	aria-expanded="false"
																>
																	<i class="icon-xs" data-feather="more-vertical"></i>
																</a>
																<div class="dropdown-menu" aria-labelledby="dropdownTeamOne">
																	<a class="dropdown-item d-flex align-items-center" href="javascript:void(0);" onclick="admissionapproved(${profile.id})">approved</a>
																	<a class="dropdown-item d-flex align-items-center" href="#!">Reject</a>
																</div>
															</div>
														</td>
													
               `
                        ;


                    tbody.appendChild(tr);
                });
                feather.replace();

                totalpages = res.data.num_pages;
                currentpage = res.data.current_page;
                pagination()







            }).catch(error => {
                console.error('Error fetching pending admissions:', error);

            });

    }function pagination() {
       if (currentpage > 1) {
        prevsbtn.style.visibility = 'visible';
        
       }else{
         prevsbtn.style.visibility = 'hidden';

      
       }

       if (currentpage < totalpages) {
        nextpagebtn.style.visibility = 'visible';

        
       }else{
        nextpagebtn.style.visibility = 'hidden';

        
       };

       prevsbtn.onclick = () =>{
        if (currentpage > 1) {
            fetchpending(currentpage - 1);
            
            
        }
    
    };


        nextpagebtn.onclick = () =>{
            if (currentpage < totalpages) {
                fetchpending(currentpage + 1);
                
                
            }
       };


        
    }



    window.fetchpending = fetchpending;

    fetchpending(1)
    setInterval(function() {
        fetchpending(currentpage);
    }, 30000);
    // setInterval(fetchpending, 30000)



});

    const laoder =document.getElementById('loadermain')
    
    



window.admissionapproved=function (profile_id) {
    laoder.style.display="block"
    
    axios.get(`approved_admin/${profile_id}`)
        .then(res => {




            Swal.fire({
                position: 'top-end',
                icon: 'success',
                title: 'Admission Approved Successfully',
                showConfirmButton: false,
                timer: 1500 // 1.5 seconds

            }).then(() => {
                fetchpending()
                 laoder.style.display="none"

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


