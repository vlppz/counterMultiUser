window.onload = function (){
	var k = document.getElementsByTagName("button")
	k[0].onclick = function (){
		var txt = document.getElementById("txt")
		txt.innerHTML = Number(txt.innerHTML)+1
	}
	k[1].onclick = function (){
		var txt = document.getElementById("txt")
		if (Number(txt.innerHTML)-1 < 0) {
			alert('Number mustn\'t be smaller, than zero!');
		} else {
			txt.innerHTML = Number(txt.innerHTML)-1
		}
	}
	k[2].onclick = function (){
		var txt = document.getElementById("txt")
		window.location.href = '/counterSave?cnt='+txt.innerHTML
	}
	k[3].onclick = function (){
		window.location.href = '/'
	}
}
