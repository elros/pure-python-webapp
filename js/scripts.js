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


function checkCommentForm() {
    var firstNameInput = document.getElementById('first_name_input');
    var lastNameInput = document.getElementById('last_name_input');
    var feedbackTextInput = document.getElementById('feedback_text_input');

    var firstName = firstNameInput.value;
    var lastName =lastNameInput.value;
    var feedbackText = feedbackTextInput.value;

    var formIsValid = ((firstName != '') && (lastName != '') && (feedbackText != ''));

    if (!formIsValid) {
        function markIfInvalid(input) {
            if (input.value == '') {
                input.style.background = '#fee';
            } else {
                input.style.background = '#fff';
            }
        }

        markIfInvalid(firstNameInput);
        markIfInvalid(lastNameInput);
        markIfInvalid(feedbackTextInput);

        return false;
    }

    return true;
}