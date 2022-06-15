const textarea = document.querySelector("textarea");
if (textarea == null) {
  console.log(textarea);
} else {
  textarea.setAttribute("cols", "100");
  textarea.setAttribute("rows", "5");
}
