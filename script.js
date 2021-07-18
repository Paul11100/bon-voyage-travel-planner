const fromWhere = document.getElementById("from")
const toWhere = document.getElementById("to")
const result = document.getElementById("result")

let x, y, z;

const change = (changeX, changeY) => {
  x = changeX
  y = changeY

  message = "Click to check route plan"
  z = [
    "https://www.google.com/maps/dir", x, y 
  ].join("/")

  result.innerHTML = `<a id="link" href=${z} target="_blank">${message}</a>`
}

fromWhere.addEventListener("input", (el) => { 
  change(el.target.value.replace(" ", "+"), y)
})

toWhere.addEventListener("input", (el) => {
  change(x, el.target.value.replace(" ", "+"))
})

toWhere.addEventListener('keyup', function (e) {
  const link = document.getElementById("link")
  if (e.keyCode === 13) {
    link.click()
  }
});
