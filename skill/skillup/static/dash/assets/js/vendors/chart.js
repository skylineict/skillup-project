document.addEventListener('DOMContentLoaded', function () {
    let chart;
   

    const fetchdatachart = () => {
        axios.get('/backend/student')
        .then(res =>{
            const datas = res.data;
            // console.log(datas)
            const facutlydatas = datas.data.faculty_data.map(faultydata => faultydata.faculty_name)
            const admittedstudent = datas.data.faculty_data.map(faultydata => faultydata.admitted_students)
            const total_students = datas.data.faculty_data.map(faultydata => faultydata.total_students)
            

            // console.log(facutlydatas)
            
            const series =[
                
                {
                name: 'Admitted Students',
                data: admittedstudent
            },
            
            {
                name: 'Rgistered Students',
                data: total_students
            }
        
        ];

            var options = {
            chart: {
                type: 'bar',
                height: 400,
                stacked: true
            },
            series: series,
            
            xaxis: {
                categories: facutlydatas
            },
            colors: ['#2E3092', '#D3D3D3'],


            title: {
                text: 'Admitted Students by Faculty',
                align: 'left',
                style: {
                    fontSize: '18px',
                    color: '#28a745'
                }
            },
            yaxis: {
                title: {
                    text: 'Number of Students'
                }
            },
            dataLabels: {
                enabled: false
            },
            legend: {
                position: 'top'
            }
        };
        
        if (!chart) {
            chart = new ApexCharts(document.querySelector("#visitorBlog"), options);
            chart.render();
            
        }else{

            chart.updateOptions({
                xaxis: {
                    categories: facutlydatas
                },
                series: series

            });
        }

       


        
        
        })
        .catch(error =>{
            console.error('Error fetching data:', error);

        });


    };

    fetchdatachart();
    // console.log(fetchdatachart)

  
    setInterval(fetchdatachart, 20000);
  
        
   

    });
      

 

   