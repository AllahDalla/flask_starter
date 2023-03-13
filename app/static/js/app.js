/* Add your Application JavaScript */
// console.log('this is some JavaScript code');

function modify() {
  btn = document.getElementsByClassName("view-property-btn")

  for (let index = 0; index < btn.length; index++) {
    let element = btn[index]
    element.addEventListener("click", async (event) => {
      // await fetch("http://localhost:5000/propertiesImages/" + element.getAttribute('id'))
      window.location.href= "http://localhost:5000/propertiesImages/" + element.getAttribute('id')
    })
    
  }
}

modify();
