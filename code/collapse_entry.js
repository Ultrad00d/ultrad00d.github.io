var coll = document.getElementsByClassName("collapsible-button");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("collapsible-open");
    var content = this.nextElementSibling;
    content.classList.toggle("collapsible-open");
    if (content.style.maxHeight){
      content.style.maxHeight = null;

      // content.style.width = null;
      // content.style.transform = null;
      // content.style.padding = null;

      this.style.width = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";

      // content.style.width = "calc(100%)";
      // content.style.transform = "translateX(calc(-2vw - 2px))";
      // content.style.padding = "0 2vw";

      // this.style.width = "100%";
    } 
  });
}