$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/films/?format=json',
    success: function (data) {
      const titles = data.results;
      console.log(titles);
      for (const key in titles) {
        const title = titles[key].title;
        console.log(titles[key].title);
        $('#list_movies').append(`<li>${title}</li>`);
      }
    }
  });
});
