(function() {
    var updateButton1 = document.getElementById('degree');
    var cancelButton1 = document.getElementById('cancelDegree');
    var favDialog1 = document.getElementById('thesisDegree');
    var updateButton2 = document.getElementById('bachelor');	  
    var cancelButton2 = document.getElementById('cancelBachelor'); 
    var favDialog2 = document.getElementById('thesisBachelor');
    
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
	  
  })();
