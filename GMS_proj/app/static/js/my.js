// var table = $('#example').DataTable();

// new $.fn.dataTable.FixedHeader(table, {
//     header:true,
// });
$(document).ready(function () {

$("#registration_button_id").click(function (e) {
    alert('clicked');
 });
});
function loadContent(url) {
    
/////////////////

 /////////////////
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById('content').innerHTML = html;
            if (url == 'view_all_complaint_admin' || url == 'specific_complaint') {
                $('#example').DataTable({
                    fixedHeader: true,
                    pageLength : 5,
      lengthMenu: [[5, 10, 20,50,100 -1], [5, 10, 20,50,100]],
                });





            }
            if (url.includes('login')) {
                (function () {
                    'use strict';
                
                    // Fetch all the forms we want to apply custom Bootstrap validation styles to
                    var forms = document.querySelectorAll('.needs-validation');
                
                    // Loop over them and prevent submission
                    Array.from(forms).forEach(function (form) {
                        form.addEventListener('submit', function (event) {
                            if (!form.checkValidity()) {
                                event.preventDefault();
                                event.stopPropagation();
                            }
                
                            form.classList.add('was-validated');
                        }, false);
                    });
                })();
            }
        })
        .catch(error => console.error('Error fetching content:', error));
        
}




//--------------------------Login Validation -------------------

