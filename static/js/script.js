function sleep(waitSec, callbackFunc) {
    // �o�ߎ��ԁi�b�j
    var spanedSec = 0;

    // 1�b�Ԋu�Ŗ����֐������s
    var id = setInterval(function () {

        spanedSec++;

        // �o�ߎ��� >= �ҋ@���Ԃ̏ꍇ�A�ҋ@�I���B
        if (spanedSec >= waitSec) {

            // �^�C�}�[��~
            clearInterval(id);

            // �������A�R�[���o�b�N�֐������s
            if (callbackFunc) callbackFunc();
        }
    }, 1000);

}

$(function () {
    $("#btn_upload").on("click", function (event) {
        $("#upload").click();
        return false;
    });

    $('#upload').change(function () {
        $('#mdl_loading').fadeIn();

        sleep(0.1, function () {
            $("#btn_submit").click();
        });
    });

    $('#btn_info').click(function () {
        $('#mdl_info').fadeIn();
    });

    $('.close_icon').click(function () {
        $('#mdl_info').fadeOut();
    });
});
