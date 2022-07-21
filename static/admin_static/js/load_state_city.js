/* load windows print button */

function printpage() {
    window.print();
}



/* load all state and city with ajax */

  
    $("#id_country").change(function () {
        const url = $("#StudentForm").attr("data-state-url");  // get the url of the `load_cities` view
        const countryId = $(this).val();
        // get the selected country ID from the HTML input

        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
            data: {
                'country_id': countryId       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_state").html(data);  // replace the contents of the city input with the data that came from the server

            }
        });


    });
    $("#id_state").change(function () {
        const url = $("#StudentForm").attr("data-cities-url");  // get the url of the `load_cities` view
        const stateId = $(this).val();
        // get the selected country ID from the HTML input

        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
            data: {
                'state_id': stateId       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_city").html(data);  // replace the contents of the city input with the data that came from the server

            }
        });


    });



