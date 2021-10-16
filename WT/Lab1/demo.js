let x="",i  ;
x,i = myFunc("Yash", 564);
console.log(x, i);
let h = "Hello"
let txt = `${h} World`;
txt = txt.toUpperCase()
console.log(txt)

function myFunc(x,i) {
	console.clear()
	return x
}

function displayDate() {
	document.getElementById("date").innerHTML = Date();
}

function clearDate(){
	document.getElementById("date").innerHTML = "asdkjas\
	 \"sdfsa\" \
	 asdfas";
}