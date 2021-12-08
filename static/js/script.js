$(function () {
    $("#btn_upload").on("click", function (event) {
        $("#upload").click();
        return false;
    });

    $('#upload').change(function () {
        $('#signup_modal').fadeIn(500);
        $("#btn_submit").click();
    });

    $('#btn_explanation').click(function () {
        $('#signup_modal').fadeIn();
    });

    $('.close_icon').click(function () {
        $('#signup_modal').fadeOut();
    });
});
