function func() {

  var innerDiv = document.getElementById('firstD').innerHTML;
  document.getElementById('secondD').innerHTML=innerDiv;

  var parent = document.getElementById('thirdD');
  var child = parent.getElementsByTagName("p")[0];
  parent.removeChild(child);

  var num = Math.floor(Math.random() * 20) + 1;
  axios.get('https://pokeapi.co/api/v2/pokemon/'+ num + '/')
  .then(function (response) {
    document.getElementById('secondP').innerHTML = response.data.forms[0].name;
    document.getElementById('firstI').src = response.data.sprites.front_default;
  })
  .catch(function (error) { });


}