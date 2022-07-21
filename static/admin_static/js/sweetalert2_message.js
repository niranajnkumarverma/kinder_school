function header_delete(id) {
  swal.fire({
    title: 'warning!',
    icon: 'warning',
    text: 'do you want to delete Header Color?',
    showCancelButton: true,
    showConfirmButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    cancelButtonText: 'No',
    confirmButtonText: 'Yes',
    reverseButtons: true
  })
    .then(function (result) {
      if (result.value) {
        window.location.href = "/admin/header_delete/" + id
       
      }
    
    })
}

function footer_delete(id) {
  swal.fire({
    title: 'warning!',
    icon: 'warning',
    text: 'do you want to delete Footer Color?',
    showCancelButton: true,
    showConfirmButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    cancelButtonText: 'No',
    confirmButtonText: 'Yes',
    reverseButtons: true
  })
    .then(function (result) {
      if (result.value) {
        window.location.href = "/admin/footer_delete/" + id
       
      }
    
    })
}

function address_delete(id) {
  swal.fire({
    title: 'warning!',
    icon: 'warning',
    text: 'do you want to delete Address?',
    showCancelButton: true,
    showConfirmButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    cancelButtonText: 'No',
    confirmButtonText: 'Yes',
    reverseButtons: true
  })
    .then(function (result) {
      if (result.value) {
        window.location.href = "/admin/address_delete/" + id
       
      }
    
    })
}



function logo_delete(id) {
  swal.fire({
    title: 'warning!',
    icon: 'warning',
    text: 'do you want to delete Logo?',
    showCancelButton: true,
    showConfirmButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    cancelButtonText: 'No',
    confirmButtonText: 'Yes',
    reverseButtons: true
  })
    .then(function (result) {
      if (result.value) {
        window.location.href = "/admin/logo_delete/" + id
       
      }
    
    })
}
function title_delete(id) {
  swal.fire({
    title: 'warning!',
    icon: 'warning',
    text: 'do you want to delete Title?',
    showCancelButton: true,
    showConfirmButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    cancelButtonText: 'No',
    confirmButtonText: 'Yes',
    reverseButtons: true
  })
    .then(function (result) {
      if (result.value) {
        window.location.href = "/admin/title_delete/" + id
       
      }
    
    })
}




function delete_teacher(id) {
  swal.fire({
    title: 'warning!',
    icon: 'warning',
    text: 'do you want to delete Teacher?',
    showCancelButton: true,
    showConfirmButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    cancelButtonText: 'No',
    confirmButtonText: 'Yes',
    reverseButtons: true
  })
    .then(function (result) {
      if (result.value) {
        window.location.href = "/admin/teachers/delete_teacher/" + id
       
      }
    
    })
}




function product_delete(id) {
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
      confirmButtonText: 'Yes',
      reverseButtons: true
    })
      .then(function (result) {
        if (result.value) {
          window.location.href = "/admin/products/book_delete/" + id
          // swal.fire('Deleted', 'You successfully deleted this file', 'success')
          // http://127.0.0.1:8000/admin/products/brand_delete/7/
          //   console.log('The Ok Button was clicked.');
        }
        // else {
        //     swal.fire('Cancelled', 'Your file is still intact', 'info')
        // }
      })
  }

  function cultural_image_delete(id) {
    console.log(id)
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
          window.location.href = "/admin/image_delete/" + id
          // swal.fire('Deleted', 'You successfully deleted this file', 'success')
  
          //   console.log('The Ok Button was clicked.');
        }
        // else {
        //     swal.fire('Cancelled', 'Your file is still intact', 'info')
        // }
      })
  }


function author_delete(id) {
  swal.fire({
    title: 'warning!',
    icon: 'warning',
    text: 'do you want to delete?',
    showCancelButton: true,
    showConfirmButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    cancelButtonText: 'No',
    confirmButtonText: 'Yes',
    reverseButtons: true
  })
    .then(function (result) {
      if (result.value) {
        window.location.href = "/admin/products/author_delete/" + id
      }
    })
}
  function publisher_delete(id) {
    console.log(id)
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
      confirmButtonText: 'Yes',
      reverseButtons: true
    })
      .then(function (result) {
        if (result.value) {
          window.location.href = "/admin/products/publisher_delete/" + id
      
        }
      })
  }
  
  function video_delete(id) {
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
      confirmButtonText: 'Yes',
      reverseButtons: true
    })
      .then(function (result) {
        if (result.value) {
          window.location.href = "/admin/video_delete/" + id
          // swal.fire('Deleted', 'You successfully deleted this file', 'success')
          // http://127.0.0.1:8000/admin/home/video_delete/2
          //   console.log('The Ok Button was clicked.');
        }
        // else {
        //     swal.fire('Cancelled', 'Your file is still intact', 'info')
        // }
      })
  }
// var editor; // use a global for the submit and return data rendering in the examples
 
// $(document).ready(function() {
//     alert("kya bat hai"),
//     editor = new $.fn.dataTable.Editor( {
        
//         ajax: "",
//         table: "#myStaticDatatable",
       

//         fields: [ {
//                 label: "transaction_id:",
//                 name: "transaction_id"
//             }, {
//                 label: "tracking_no:",
//                 name: "tracking_no"
//             }, {
//                 label: "username:",
//                 name: "username"
//             }, {
//                 label: "email:",
//                 name: "email"
//             }, {
//                 label: "date_ordered:",
//                 name: "date_ordered"
//             }, {
//                 label: "status:",
//                 name: "status",
               
//             }, {
//                 label: "total_price:",
//                 name: "salartotal_pricey"
//             }
            
//         ]
//     } );
 
//     var editIcon = function ( data, type, row ) {
//         if ( type === 'display' ) {
//             return data + ' <i class="fa fa-pencil"/>';
//         }
//         return data;
//     };
 
//     $('#myStaticDatatable tbody').on( 'click', 'td i', function (e) {
//         e.stopImmediatePropagation(); // stop the row selection when clicking on an icon
 
//         editor.inline( $(this).parent() );
//     } );
 
//     $('#myStaticDatatable').DataTable( {
//         dom: "Bfrtip",
//         ajax: "../php/staff.php",
//         columns: [
//             { data: "first_name", render: editIcon },
//             { data: "last_name",  render: editIcon },
//             { data: "position",   render: editIcon },
//             { data: "office",     render: editIcon },
//             { data: "start_date", render: editIcon },
//             { data: "salary",     render: function ( data, type, row ) {
//                 if ( type === 'display' ) {
//                     var numberRenderer = $.fn.dataTable.render.number( ',', '.', 0, '$' ).display;
//                     return numberRenderer( data )+ ' <i class="fa fa-pencil"/>';
//                 }
//                 return data;
//             } }
//         ],
//         select: true,
//         buttons: [
//             { extend: "create", editor: editor },
//             { extend: "edit",   editor: editor },
//             { extend: "remove", editor: editor }
//         ]
//     } );
// } );


