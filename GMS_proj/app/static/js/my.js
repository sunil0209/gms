// var table = $('#example').DataTable();

// new $.fn.dataTable.FixedHeader(table, {
//     header:true,
// // });
// $(document).ready(function () {

//     $("#registration_button_id").click(function (e) {
//         alert('clicked');
//      });
//     });
/////@@@### User _registration

document.getElementById('registration_button_id').addEventListener('click', function() {
    // Get form data
    var formData = new FormData(document.getElementById('registration_form_id'));
  
    // Make a fetch request to the server
    fetch("{% url 'user_registration' %}", {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': '{{ csrf_token }}',  // Include CSRF token if using Django
      },
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.text();
    })
    .then(html => {
      // Insert the loaded content into the container
      document.getElementById('content').innerHTML = html;
    })
    .catch(error => console.error('Error loading content:', error));
  });
  

/////////##### Define a function to load content
function loadContent(url) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById('content').innerHTML = html;

            // Check if the url is 'view_all_complaint_admin'
            if (url === 'user_registration') {
                // Add your jQuery click event handling here
                $("#registration_button_id").click(function (e) {
                    alert('clicked');
                });
            }
        })
        .catch(error => {
            console.error('Error fetching content:', error);
        });
}

// Attach the click event to an anchor element with an onclick attribute
// In this example, the anchor element has id="load_content_link"
document.getElementById('load_content_link').onclick = function() {
    // Get the URL from the href attribute of the anchor element
    var url = this.href;

    // Call the loadContent function with the URL
    loadContent(url);

    // Prevent the default behavior of the anchor element
    return false;
};

/////user_registration


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
    
    ///user_registration onload content


