$(function () {
    $("#btn_upload").on("click", function (event) {
        $("#upload").click();
        return false;
    });

    $('#upload').change(function () {
        $("#btn_submit").click();
    });
});
