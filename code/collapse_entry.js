var coll = document.getElementsByClassName("collapsible-button");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("collapsible-open");
    var content = this.nextElementSibling;
    content.classList.toggle("collapsible-open");
    if (content.style.maxHeight){
      content.style.maxHeight = null;
      this.style.width = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}
