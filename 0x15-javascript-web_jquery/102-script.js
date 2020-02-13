$(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const langCode = $('INPUT#language_code').val();
    console.log(langCode)
    $.ajax({
      type: 'GET',
      url: `https://fourtonfish.com/hellosalut/?lang=${langCode}`,
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  });
});
