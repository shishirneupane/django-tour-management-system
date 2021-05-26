//Query All input fields
var form_fields = document.getElementsByTagName('input')

form_fields[1].placeholder = 'First Name';
form_fields[2].placeholder = 'Last Name';
form_fields[3].placeholder = 'Username';
form_fields[4].placeholder = 'Email Address';
form_fields[5].placeholder = 'Password';
form_fields[6].placeholder = 'Confirm Password';


for (var field in form_fields) {
    form_fields[field].className += 'form-control'
}
