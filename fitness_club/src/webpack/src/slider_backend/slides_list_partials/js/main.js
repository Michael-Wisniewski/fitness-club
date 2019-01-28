import '../../../base_templates/backend_partials/js/main.js';
import 'jquery-ui/ui/core';
import 'jquery-ui/ui/widgets/sortable';
window.$ = require('jquery');
import 'jquery.cookie';

var $sortable_ul = $('#sortable_ul');
var $modal = $('#savingModal');

var updateSlidesOrder = function(event, ui) {
    $modal.addClass('show');
    var $dropped_li = ui.item;
    var slide_id = $dropped_li.attr('slide_id');
    var slide_order = $sortable_ul.find('li').index($dropped_li)+1;

    $.ajax(
        {
            type: "POST",
            url: urls['slides_order'],
            data: {
                slide_id: slide_id,
                slide_order: slide_order
            },
            success: function(data) {
                if(data.operation_status == 'OK') {
                    var $list_items = $sortable_ul.find('li');
                    $list_items.each(function(index){
                        $(this).find('.number').text(index+1);
                    });
                    $modal.removeClass('show');
                }
                else {
                    location.reload();
                }
            }
        }
    )
};

$sortable_ul.sortable({
    update: updateSlidesOrder
});


