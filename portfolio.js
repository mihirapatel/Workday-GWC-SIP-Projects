var gifWidth = 200;
var gifHeight = 200;

var screenshotWidth = 520;
var screenshotHeight = 330;


function welcome () {
  alert("Hello World!")
}
welcome();

function getBig (x) {
		x.style.width = "820px";
		x.style.height = "630px";
}

function getNormal (x) {
	x.style.width = "520px";
	x.style.height = "330px";	
}
 
function showText () {
	document.getElementById("paraaboutme").innerHTML = "My name is Mihira Patel and I am a rising junior at Washington High School in Fremont, California.";
}


