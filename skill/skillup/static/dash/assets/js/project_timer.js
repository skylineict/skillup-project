document.addEventListener('DOMContentLoaded', function () {
    const enddateEl = document.getElementById('countdown')
    const enddate = new Date(enddateEl.dataset.enddate).getTime();
    function UpdateProjectCountdown() {
        const timenow = new Date().getTime();
        const timeLeft = enddate - timenow
        // console.log(timeleft)
        if (timeLeft <=0) {
            enddateEl.innerHTML = "Porject has expired";
            
        }

        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        enddateEl.innerHTML =      days + "d " + hours + "h " + minutes + "m " + seconds + "s ";


        
    }
    // console.log(enddate)
    // console.log(enddateEl)
    setInterval(UpdateProjectCountdown, 1000);
    
    // UpdateProjectCountdown()

})