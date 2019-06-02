var msg;
var nick_name;
var time;

function pressed() {
  // when you press enter contents of the input will save in msg
  msg = document.getElementById("message").value;
  nick_name = document.getElementById("myName").value
  var d = new Date();
  time = d.getFullYear() + "-" + ( d.getMonth() + 1 ) + "-" + d.getDate() + " " + d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds();
}

 function Request(){
     var requestParam ="";
     this.getParameter = function(param){
     var url = unescape(location.href);
     var paramArr = (url.substring(url.indexOf("?")+1,url.length)).split("&");

     for(var i = 0 ; i < paramArr.length ; i++){
        var temp = paramArr[i].split("=");
        if(temp[0].toUpperCase() == param.toUpperCase()){
         requestParam = paramArr[i].split("=")[1];
         break;
        }
    }
    return requestParam;
   }
}

// 페이지를 띄우면서 서버에서 대화 내용을 가져와서 띄워줌
/*window.onload = function () {
  axios.get('server url')
  .then(function (response) {
    document.getElementById('conversation').innerHTML = response.data.~;
  })
  // 유저 목록 가져와서 띄워줌
    axios.get('server url')
  .then(function (response) {
    document.getElementById('userList').innerHTML = response.data.~;
  })
}*/
