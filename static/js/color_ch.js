function change_imgfile() {
    $('#div_img_file').css('display', 'none');
    $('#img_preview').attr('src', URL.createObjectURL($('#img')[0].files[0]));
    $('#img_preview').css('display', 'block');
}

function change_img() {
    $('#img').click();
}