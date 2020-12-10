let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/about.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
  const jsonObj = request.response;
  const textAbout = jsonObj['about']; 
  document.getElementById('motivation').innerHTML = textAbout['motivation'];
  document.getElementById('content').innerHTML = textAbout['content'];
  document.getElementById("trad-about").innerHTML = "<button onclick='espTrad()' style='float: right;'>Read in Spanish</button>";
  document.getElementById('commentary').innerHTML = textAbout['commentary'][0] + '<br><br>' + textAbout['commentary'][1] + '<br><br>' + textAbout['commentary'][2] + '<br><br>' + textAbout['commentary'][3];
  document.getElementById("trad-about").innerHTML = "<button onclick='espTrad()' style='float: right;'>Read in Spanish</button>";
}

function espTrad() {
let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/about.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
const jsonObj = request.response;
const textAbout = jsonObj['traduction']; 
document.getElementById('motivation').innerHTML = textAbout['motivacion'];
document.getElementById('content').innerHTML = textAbout['contenido'];
document.getElementById('commentary').innerHTML = textAbout['comentario'][0] + '<br><br>' + textAbout['comentario'][1] + '<br><br>' + textAbout['comentario'][2] + '<br><br>' + textAbout['comentario'][3];
document.getElementById("trad-about").innerHTML = "<button onclick='enTrad()' style='float: right;'>Read in English</button>";
  }			
}

function enTrad() {
let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/about.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
const jsonObj = request.response;
const textAbout = jsonObj['about']; 
document.getElementById('motivation').innerHTML = textAbout['motivation'];
document.getElementById('content').innerHTML = textAbout['content'];
document.getElementById('commentary').innerHTML = textAbout['commentary'][0] + '<br><br>' + textAbout['commentary'][1] + '<br><br>' + textAbout['commentary'][2] + '<br><br>' + textAbout['commentary'][3];
document.getElementById("trad-about").innerHTML = "<button onclick='espTrad()' style='float: right;'>Read in Spanish</button>";
  }
}
