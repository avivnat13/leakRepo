const el = element.innerHTML;
const el13 = element.innerHTML;

function bad1(userInput) {
// ruleid: insecure-document-method
  el.innerHTML = '<div>' + userInput + '</div>';
avivnat13 marked this conversation as resolved.
}

function bad2(userInput) {
// ruleid: insecure-document-method
  document.body.outerHTML = userInput;
avivnat13 marked this conversation as resolved.
}

function bad3(userInput) {
  const name = '<div>' + userInput + '</div>';
// ruleid: insecure-document-method
  document.write(name);
avivnat13 marked this conversation as resolved.
}

function ok1() {
  const name = "<div>it's ok</div>";
// ok: insecure-document-method
  el.innerHTML = name;
}

function ok2() {
// ok: insecure-document-method
  document.write("<div>it's ok</div>");
}


// ruleid:dom-based-xss
document.write("<OPTION value=1>"+document.location.href.substring(document.location.href.indexOf("default=")+8)+"</OPTION>");
