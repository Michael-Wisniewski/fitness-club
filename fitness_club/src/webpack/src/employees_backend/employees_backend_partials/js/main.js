import '../../../base_templates/backend_partials/js/main.js';
window.$ = require('jquery');
import 'datatables';

var renderEditButton = function(data, type, row) {
    var button = '<a href="' + urls['employee_edit_blind'] + data + '/">'+
                     '<button class="btn btn-edit">Edit</button>'+
                 '</a>';
    return button;
};

var renderDeleteButton = function(data, type, row) {
    var button = '<a href="' + urls['employee_delete_blind']+ data + '/">'+
                    '<button class="btn btn-danger">Delete</button>'+
                '</a>';
    return button;
}

var config = {
    "ajax": {
        url: urls['employees_list_data'],
        dataSrc: 'data'
    },
    "columnDefs": [ {
            "targets": 0,
            "data": null,
            "defaultContent": '',
            "orderable" : false,
            "searchable": false,
        }, 
        { 
            "targets": 1,    
            "data": "first_name",
            orderData: [ 1, 2 ]
        },
        { 
            "targets": 2,
            "data": "last_name"
        },
        {
            "targets": 3,
            "data": "email"
        },
        {
            "targets": 4,
            "data": "id",
            "orderable": false,
            "searchable": false,
            "render": renderEditButton,
            "className": 'text-center'
        },
        {
            "targets": 5,
            "data": "id",
            "orderable": false,
            "searchable": false,
            "render": renderDeleteButton,
            "className": 'text-center'
        }
    ],
    "order": [[ 1, 'desc' ]]
};

$(document).ready(function() {
    var tableObj = $('#list').DataTable(config);
    tableObj.on( 'order.dt search.dt', function () {
        tableObj.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();
});