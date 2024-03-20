var table = $('#example').DataTable({
  header: true,
  lengthMenu: [
    [5, 10, 25, 50, -1],
    ['5', '10', '25', '50', 'All']
  ]
});

// showing password Requirements
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
});



//Validating Froma
function validateForm() {
  // Phone NO check
  var phoneNumberInput = document.getElementById("phone_no");

  // Add an event listener to the phone number field to check for 10 digits
  phoneNumberInput.addEventListener("input", function () {
    var phoneNumber = phoneNumberInput.value;

    // Remove non-numeric characters
    phoneNumber = phoneNumber.replace(/\D/g, '');

    if (phoneNumber.length === 10) {
      // Valid phone number
      phoneNumberInput.setCustomValidity("");
    } else {
      // Invalid phone number
      phoneNumberInput.setCustomValidity("Phone number must have exactly 10 digits");
    }
  });

  // Validating password
  var password = document.getElementById("password").value;
  var confirmPassword = document.getElementById("confirm_password").value;
  var errorDiv = document.getElementById("error");

  if (password !== confirmPassword) {
    document.getElementById("confirm_password").classList.remove("match");
    document.getElementById("confirm_password").classList.add("no-match");
    errorDiv.innerHTML = "Error: Passwords do not match";
    return false;
  } else {
    document.getElementById("confirm_password").classList.remove("no-match");
    document.getElementById("confirm_password").classList.add("match");
    document.getElementById("password").classList.add("match");
    errorDiv.innerHTML = "";
    return true;
  }
}
