/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
    sessionStorage.setItem("display", "none");
  }
  
  function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      txtValue = a[i].textContent || a[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }

function onClick(){
  if (sessionStorage.getItem("display") != "block"){
    sessionStorage.setItem("display", "block");
  }
  else{
    sessionStorage.setItem("display", "none");
  }
  document.getElementById("matchTable").style.display = sessionStorage.getItem("display");
}