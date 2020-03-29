chrome.runtime.onInstalled.addListener(()=> {
    console.log("Installed");
    query_for_tabs();
});


chrome.bookmarks.onCreated.addListener(()=>{
    alert("Bookmark  Created");
});


function  query_for_tabs() {
    var query_info = {};

    chrome.tabs.query(query_info, tabs => {
        console.log("Total tabs open: " + tabs.length);
        console.log(tabs);
    });

}


