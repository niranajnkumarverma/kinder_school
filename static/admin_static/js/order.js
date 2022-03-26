$(document).ready(function () {
    $('#myStaticDatatable').DataTable();
    
});




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


