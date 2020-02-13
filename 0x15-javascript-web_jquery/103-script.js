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
  $('INPUT#language_code').keypress(function (e) {
    const key = e.which;
    if (key === 13) {
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
    }
  });
});
