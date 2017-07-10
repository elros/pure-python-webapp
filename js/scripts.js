function loadCitiesForSelectedRegion() {
    var selectbox = document.getElementById("city_selector");

    removeSelectOptions(selectbox);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            if (response.success) {
                response.data.cities.forEach(function(city){
                    var option = document.createElement("option");
                    option.text = city.name;
                    option.value = city.id;
                    selectbox.add(option);
                });
                selectbox.disabled = false;
            }
        }
    };
    var region_id = document.getElementById("region_selector").value;
    var api_path = "/region/" + region_id + "/cities/";
    xhttp.open("GET", api_path, true);
    xhttp.send();
}

function removeSelectOptions(selectbox) {
    for(var i = selectbox.options.length - 1 ; i >= 0 ; i--) {
        selectbox.remove(i);
    }
}

function isNotEmpty(it){
    return (it != '');
}

function isValidPhoneNumber(it){
    return (it.match(/\(\d+\)\d+/));
};

function isValidEmail(it){
        rfc5322_email_regex = new RegExp('^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$');
        return it.match(rfc5322_email_regex);
    };


function checkCommentForm() {
    function markIfInvalid(input, validator) {
        if (!validator(input.value)) {
            input.style.background = '#fee';
        } else {
            input.style.background = '#fff';
        }
    }

    var firstNameInput = document.getElementById('first_name_input');
    var lastNameInput = document.getElementById('last_name_input');
    var feedbackTextInput = document.getElementById('feedback_text_input');
    var phoneNumberInput = document.getElementById('phone_number_input');
    var emailInput = document.getElementById('email_input');

    var firstName = firstNameInput.value;
    var lastName = lastNameInput.value;
    var feedbackText = feedbackTextInput.value;
    var phoneNumber = phoneNumberInput.value;
    var email = emailInput.value;

    var mandatoryFieldsAreNotEmpty = isNotEmpty(firstName) && isNotEmpty(lastName) && isNotEmpty(feedbackText);
    var phoneNumberIsValid = isValidPhoneNumber(phoneNumber);
    var emailIsValid = isValidEmail(email);

    var canPostForm = true;

     markIfInvalid(firstNameInput, isNotEmpty);
     markIfInvalid(lastNameInput, isNotEmpty);
     markIfInvalid(feedbackTextInput, isNotEmpty);

    if (!mandatoryFieldsAreNotEmpty) {
        canPostForm = false;
    }

    if (isNotEmpty(phoneNumber) && !phoneNumberIsValid) {
        markIfInvalid(phoneNumberInput, isValidPhoneNumber);
        canPostForm = false;
    }

    if (isNotEmpty(email) && !emailIsValid) {
        markIfInvalid(emailInput, isValidEmail);
        canPostForm = false;
    }

    return canPostForm;
}