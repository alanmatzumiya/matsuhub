function init () {
  document.getElementById("text-init").innerHTML = "<h4>A <a href='https://en.wikipedia.org/wiki/Mathematician'>Mathematician</a> and Engineer; But <br />I'm also a <a href='https://en.wikipedia.org/wiki/Programmer'>Programmer</a>.</h4>";
  document.getElementById("mybtn").innerHTML = "<button onclick='stop()'><h4>Hi! I'm Alan Matzumiya</h4></button>";
  }
function stop () {
  document.getElementById("text-init").innerHTML = "";
  document.getElementById("mybtn").innerHTML = "<button onclick='init()'><h4>Click Me!</h4></button>";
  }
