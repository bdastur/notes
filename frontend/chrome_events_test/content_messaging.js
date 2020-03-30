window.onload(testMessage('On window load'));


function testMessage(msg_text) {
	console.log("Send a test message");
	chrome.runtime.sendMessage({payload: msg_text},
	() => console.log(2 + 2));

    console.log("Message sent!");
}


function payload_response() {
	console.log("This is the response");
	console.log(2+2);
}


window.focus(testMessage("Window focus!"));