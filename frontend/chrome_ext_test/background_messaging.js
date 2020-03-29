chrome.runtime.onMessage.addListener((request,  sender,  resp) => {
	console.log("Request: " + request);
	console.dir(request);
	console.log("sender: " + sender);
	console.dir(sender);
	print_sender_details(sender);
	console.log("call resp callback: " + resp());
});

function print_sender_details(sender) {
    console.log("Sender url: " + sender.url);
}

var query_info = {
	"active": true,
	"currentWindow": true
};

chrome.tabs.query(query_info, tabs => {
	chrome.tabs.sendMessage(tabs[0].id, {name: 'Behzad'});
});