$(document).ready(function () {
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-product .modal-content").html("");
                $("#modal-product").modal("show");
            },
            success: function (data) {
                $("#modal-product .modal-content").html(data.html_form);
            }
        });
    };
    /* Binding */
    $(".js-create-product").click(loadForm);
});