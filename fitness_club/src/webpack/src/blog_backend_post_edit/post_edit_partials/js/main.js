import '../../../base_templates/backend_partials/js/main.js';
import 'pc-bootstrap4-datetimepicker';

$(document).ready(function(){
    $('#datetimepicker input').datetimepicker({
        format:'YYYY-MM-DD HH:mm:ss',
    });
});