import '../../../base_templates/backend_partials/js/main.js';
window.$ = require('jquery');
import 'datatables';

var renderAuthor = function(data, type, row) {
    var author = data.first_name + ' ' + data.last_name;
    return author;
};

var renderEditButton = function(data, type, row) {
    var button = '<a href="' + urls['post_edit_blind'] + data + '/">'+
                     '<button class="btn btn-edit">Edit</button>'+
                 '</a>';
    return button;
};

var renderDeleteButton = function(data, type, row) {
    var button = '<a href="' + urls['post_delete_blind']+ data + '/">'+
                    '<button class="btn btn-danger">Delete</button>'+
                '</a>';
    return button;
}

var config = {
    "ajax": {
        url: urls['posts_list_data'],
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
            "data": "title",
        },
        { 
            "targets": 2,
            "data": "author",
            "render": renderAuthor,
        },
        {
            "targets": 3,
            "data": "publish"
        },
        { 
            "targets": 4,
            "data": "status" 
        },
        {
            "targets": 5,
            "data": "id",
            "orderable": false,
            "searchable": false,
            "render": renderEditButton,
            "className": 'text-center'
        },
        {
            "targets": 6,
            "data": "id",
            "orderable": false,
            "searchable": false,
            "render": renderDeleteButton,
            "className": 'text-center'
        }
    ],
    "order": [[ 3, 'desc' ]]
};

$(document).ready(function() {
    var tableObj = $('#posts_list').DataTable(config);
    tableObj.on( 'order.dt search.dt', function () {
        tableObj.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();
});