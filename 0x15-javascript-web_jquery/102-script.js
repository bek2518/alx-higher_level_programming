const $ = window.$;
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
    const input = $('INPUT#language_code').val();
    $.get(url + input, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
