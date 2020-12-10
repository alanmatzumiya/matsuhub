let URL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
let requestProjects = new XMLHttpRequest();
requestProjects.open('GET', URL);
requestProjects.responseType = 'json';
requestProjects.send();

requestProjects.onload = function() {
  const jsonProjects = requestProjects.response;
  document.getElementById('desc-git').innerHTML = jsonProjects['description'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showTrad()' style='float: right;'>Read in Spanish</button>";
}

function showDescript() {
  let URL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
  let requestProjects = new XMLHttpRequest();
  requestProjects.open('GET', URL);
  requestProjects.responseType = 'json';
  requestProjects.send();

  requestProjects.onload = function() {
  const jsonProjects = requestProjects.response;
  document.getElementById('desc-git').innerHTML = jsonProjects['description'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showTrad()' style='float: right;'>Read in Spanish</button>";
  }
}			

function showTrad() {
  let URL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
  let requestProjects = new XMLHttpRequest();
  requestProjects.open('GET', URL);
  requestProjects.responseType = 'json';
  requestProjects.send();

  requestProjects.onload = function() {
  const jsonProjects = requestProjects.response;
  document.getElementById('desc-git').innerHTML = jsonProjects['traduction'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showDescript()' style='float: right;'>Read in English</button>";
  }
}

(function() {
    var updateButton1 = document.getElementById('pyFPK');
    var cancelButton1 = document.getElementById('cancelFPK');
    var favDialog1 = document.getElementById('descriptionFPK');
    var updateButton2 = document.getElementById('pyPDE');	  
    var cancelButton2 = document.getElementById('cancelPDE'); 
    var favDialog2 = document.getElementById('descriptionPDE');
    var updateButton3 = document.getElementById('pyCourses');
    var cancelButton3 = document.getElementById('cancelCourses');
    var favDialog3 = document.getElementById('descriptionCourses');
    // Update button opens a modal dialog
    updateButton1.addEventListener('click', function() {
      favDialog1.showModal();
    });

    // Form cancel button closes the dialog box
    cancelButton1.addEventListener('click', function() {
      favDialog1.close();
    });
    // Update button opens a modal dialog
    updateButton2.addEventListener('click', function() {
      favDialog2.showModal();
    });

    // Form cancel button closes the dialog box
    cancelButton2.addEventListener('click', function() {
      favDialog2.close();
    });
	  
    // Update button opens a modal dialog
    updateButton3.addEventListener('click', function() {
      favDialog3.showModal();
    });

    // Form cancel button closes the dialog box
    cancelButton3.addEventListener('click', function() {
      favDialog3.close();
    });
        
  })();
