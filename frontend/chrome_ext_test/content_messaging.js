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

chrome.tabs.onActivated.addListener(tab_activated);

function tab_activated(active_info) {
	console.log("Tab activated " + active_info);
	testMessage('Tab activated');
}

chrome.tabs.onRemoved.addListener(tab_removed);

function tab_removed(active_info) {
	console.log("Tab removed " + active_info);
	testMessage('Tab removed');
}

window.focus(testMessage("Window focus!"));