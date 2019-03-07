import '../../../base_templates/backend_partials/js/main.js';
import 'bootstrap/js/dist/modal';
import 'pc-bootstrap4-datetimepicker';
import Cropper from 'cropperjs';

$(document).ready(function(){

    $('#datetimepicker input').datetimepicker({
        format:'YYYY-MM-DD HH:mm:ss',
    });

    const $window = $(window)
    var $modal = $('#imageModal');
    var $cropper_container = $('.modal-body');
    var $input_field = $('#id_image');
    var $range_control = $('#range-control');
    var image_to_crop_el = document.getElementById('image-to-crop');
    var $crop_button = $('#crop-button');
    var cropper;
    var imageCroppedFlag = false;
    var initial_zoom_ratio = 0;
    var conf = {
        aspectRatio: 1 / 0.666666667,
        scalable: false,
        viewMode: 3,
        movable: true,
        cropBoxMovable: false,
        cropBoxResizable: false, 
        dragMode: 'move',
        autoCropArea: 1,
        minContainerWidth: 750,
        minContainerHeight:  500,
    };

    $input_field.change(function(){
        loadImage(this);
    });

    $(window).resize(updateCropDimensions);

    function updateCropDimensions() {
        var width = $(window).width();
        var minContainerWidth, minContainerHeight;

        if (width > 992) {
            minContainerWidth = 750;
            minContainerHeight = 500;
        }
        else if(width <= 992 && width > 576) {
            minContainerWidth = 450;
            minContainerHeight = 300;
        }
        else {
            minContainerWidth = width - 50;
            minContainerHeight = Math.ceil(minContainerWidth/1.5);
        }

        if (conf.minContainerWidth != minContainerWidth) {
            conf.minContainerWidth = minContainerWidth;
            conf.minContainerHeight = minContainerHeight;
            upCropper();
        }
    };

    function loadImage(input) {
        if(input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                $(image_to_crop_el).attr('src', e.target.result);
                upCropper();
                $modal.modal("show");
            }
            reader.readAsDataURL(input.files[0]);
        }
    };
    
    function upCropper(){
        if(typeof cropper != 'undefined') {
            cropper.destroy();
        }
        else {
            updateCropDimensions();
        }
        cropper = new Cropper(image_to_crop_el, conf);
    };

    $cropper_container.on('ready', function () {
        var image_data = cropper.getImageData();
        initial_zoom_ratio = (image_data.width / image_data.naturalWidth) * 100;
        $range_control.attr('min', initial_zoom_ratio);
        $range_control.val(initial_zoom_ratio);
    });

    $cropper_container.on('zoom input', function(e) {
        if(e.type == 'zoom'){
            var new_ratio = e.originalEvent.detail.ratio;
            if (new_ratio > 1) {
                e.preventDefault();
                cropper.zoomTo(1);
            }
            else if (new_ratio < 0) {
                e.preventDefault();
                cropper.zoomTo(0);
            }
            else {
                var ratio_in_percent = ((new_ratio) * 100)
                $range_control.val(ratio_in_percent);
            }
        }
        else {
            var new_ratio = (e.originalEvent.originalTarget.valueAsNumber / 100);
            cropper.zoomTo(new_ratio);
        }
    });

    $crop_button.on('click', function(e){
        e.stopPropagation();
        var data = cropper.getData(true);
        $('#id_x').val(data['x']);
        $('#id_y').val(data['y']);
        $('#id_width').val(data['width']);
        $('#id_height').val(data['height']);
        imageCroppedFlag = true;
        $modal.modal('hide');
    });

    $modal.on('hidden.bs.modal', function (e) {
        if(!imageCroppedFlag){
            $input_field.val('');
        }
    })

});