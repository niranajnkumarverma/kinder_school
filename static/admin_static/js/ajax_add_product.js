

// def add_new(request):
//     if request.method == 'POST':
//         print('ajax form data: ', request.POST)
//         UserProfile.objects.create(
//             Name = request.POST.get('fullname'),
//             Email = request.POST.get('email'),
//             Mobile = request.POST.get('mobile'),
//         )
//         load_data()
        
//         l = []
//         for user_data in data['user_data']:
//             d = dict()
//             for key,value in user_data.__dict__.items():
//                 if not key.startswith('_'):
//                     d.setdefault(key, value)
//             l.append(d)
//         data['user_data'] = l
        
//         return JsonResponse(data)
//     else:
//         pass



//         <script>
// $('#myStaticDatatable').DataTable( {
//     "processing": true,
//     "serverSide": true
//     });

//  </script>




//     $(document).ready(function() {
//     $('#myStaticDatatable').DataTable( {
//         "processing": true,
//         "serverSide": true,
//         'csrfmiddlewaretoken': "{{csrf_token}}",
//         "ajax": {
//             "url": "{% url 'products:add_product_ajax' %}",
//             "type": "POST",
//         },
//         "columns": [
//         { data: 'brand_name' },
//         { data: 'product_name' },
//         { data: 'product_price' },
//         { data: 'product_image' }
            
//         ]
//     } );
// } );




    // $(document).ready(function () {
    
    //     $('#addproduct-form').submit(function (e) {
    //         e.preventDefault();
    //         var form_ele = $(this);
    //         ajax_submit(form_ele);
    //     });
    //     function ajax_submit(form) {
    //         var data = {
    //             'brand_name': form.find('input[name="brand_name"]').val(),
    //             'product_name': form.find('input[name="product_name"]').val(),
    //             'product_price': form.find('input[name="product_price"]').val(),
    //             'product_image': form.find('input[name="product_image"]').val(),
    //             'csrfmiddlewaretoken': "{{csrf_token}}"
    //         }
    //         $.ajax({
    //             type: "POST",
    //             url: "{% url 'products:add_product_ajax' %}",
    //             data: $('#addproduct-form').serialize(),
    //             // url: form.attr('action'),
    //             // data: data,
    //             success: function (response_data) {
    //                 alert('Data added successfully!')
    //                 var html_table_data = '';
    //                 for (Add_product_Ajax in response_data.user_data) {
    //                     user_data = response_data.user_data[Add_product_Ajax];

    //                     html_table_data += `<tr><td>${user_data.id}</td>
    //                     <td>${user_data.brand_name}</td>
    //                     <td>${user_data.product_name}</td>
    //                     <td>${user_data.product_price}</td>
    //                     <td>${user_data.product_image}</td>
    //                     <td>
    //                         <a href="update_data/${user_data.id}/" class="btn btn-sm btn-primary">Update</a>
    //                         <a href="delete_data/${user_data.id}/" class="btn btn-sm btn-danger">Delete</a>
    //                     </td>
    //                     </tr>`;
    //                     console.log(user_data)
    //                 }
    //                 $('tbody').html(html_table_data)
    //                 //console.table(response_data.user_data)
    //             },
    //             error: function (e) {
    //                 document.write(e.responseText);
    //                 console.log("ERROR : ", e);
    //             },
    //         });
    //     }
    
    // })

















