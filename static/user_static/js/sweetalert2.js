
function card_delete(id) {
    // console.log(id)
    // }
    swal.fire({
        title: 'warning!',
        icon: 'warning',
        text: 'do you want to delete?',
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: 'No',
        confirmButtonText: "Yes",
        reverseButtons: true
    })
        .then(function (result) {
            if (result.value) {
                window.location.href = "/order/deletecart/" + id
                // swal.fire('Deleted', 'You successfully deleted this file', 'success')
                // http://127.0.0.1:8000/order/deletecart/42/
                //   console.log('The Ok Button was clicked.');
            }
            // else {
            //     swal.fire('Cancelled', 'Your file is still intact', 'info')
            // }
        })
}



function card_exist(id) {
    // console.log(id)
    // }
    swal.fire({
        title: 'warning!',
        icon: 'warning',
        text: 'already card exist in card?',
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: "Yes",
        reverseButtons: true
    })
        .then(function (result) {
            if (result.value) {
                window.location.href = "/order/addtocart/" + id
                // swal.fire('Deleted', 'You successfully deleted this file', 'success')
                // http://127.0.0.1:8000/order/deletecart/42/
                //   console.log('The Ok Button was clicked.');
            }
            // else {
            //     swal.fire('Cancelled', 'Your file is still intact', 'info')
            // }
        })
}