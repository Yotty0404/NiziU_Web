function sleep(waitSec, callbackFunc) {
    // 経過時間（秒）
    var spanedSec = 0;

    // 1秒間隔で無名関数を実行
    var id = setInterval(function () {

        spanedSec++;

        // 経過時間 >= 待機時間の場合、待機終了。
        if (spanedSec >= waitSec) {

            // タイマー停止
            clearInterval(id);

            // 完了時、コールバック関数を実行
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
