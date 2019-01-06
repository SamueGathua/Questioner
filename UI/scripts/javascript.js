function createNew() {
    window.open( "/home/samie/Quistioner/create_meetup.html", "myWindow", "status = 1, height = 650, width = 780, resizable = 0" )
}

function deleteConfirm() {
  var r = confirm("Please confirm that you want to delete the meetup");
  if (r == true) {
  	
    alert('The record has been deleted successfully');
    
  } else {
  
  alert('The record  has Not  been deleted');
    
  }
 
}
