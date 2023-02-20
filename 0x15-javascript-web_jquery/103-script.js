const $ = window.$;
$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
  $('INPUT#btn_translate').click(function () {
    const input = $('INPUT#language_code').val();
    $.get(url + input, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#btn_translate').keypress(function (key) {
    const input = $('INPUT#language_code').value();
    if (key.keycode === 13) {
      $.get(url + input, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
