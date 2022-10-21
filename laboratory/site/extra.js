function toggle_click(button, id_str) {
  var block = document.getElementById(id_str);
  if (button.innerHTML == "Show solution") {
    block.style.display = "block";
    button.innerHTML= "Hide solution";
  } else {
    block.style.display = "none";
    button.innerHTML= "Show solution";
  }
}
