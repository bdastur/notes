/*
 * Event triggered when the extension is installed.
 */
chrome.runtime.onInstalled.addListener(()=> {
    console.log("Chrome extension Installed");
    query_for_tabs();
    create_basic_notification();
    getCPUInfo();
});


chrome.bookmarks.onCreated.addListener(()=>{
    alert("Bookmark  Created");
});


function  query_for_tabs() {
    var query_info = {};

    /*
     * Query for all tabs, since query_info does not
     * have any filters.
     */
    chrome.tabs.query(query_info, tabs => {
        console.log("Total tabs open: " + tabs.length);
    });
}


/*
 * Event is triggered when switching to a tab.
 *
 */
chrome.tabs.onActivated.addListener(tab_activated);
function tab_activated(info) {
    console.log("Tab activated! ");

    //Get info for the tab.
    chrome.tabs.get(info.tabId, get_tab_info);

    //Create a new Alarm
    var alarm_info = {
        delayInMinutes: 1
    };

    // Create a new Alarm.
    console.log("New Alarm created!");
    chrome.alarms.create("tab_active_alarm", alarm_info);

}

/*
 * Event is triggered when an alarm is triggered.
 */
chrome.alarms.onAlarm.addListener(alarmTriggered);
function alarmTriggered(alarm_info) {
    console.log("Alarm triggered: " + alarm_info);
    console.dir(alarm_info);
    alert("You are on this page too long!");
}


/*
 * Event is triggered when switching to a tab. Difference
 * between this event and onActivated is it triggered on
 * the existing tab, just before the switch.
 */
chrome.tabs.onActiveChanged.addListener(tab_active_changed);
function tab_active_changed(tab_id, tab_info) {
    console.log("Tab Active changed!: " + tab_id);
    console.log("Tab Info:")
    console.dir(tab_info);
}

/*
 * Event is triggered when the existing/active tab
 * changes - eg new URL.
 */
chrome.tabs.onUpdated.addListener(tab_on_updated);
function tab_on_updated(tab_id, change_info, tab) {
    console.log("Tab on Updated " + tab_id);
    console.dir(change_info);
    console.dir(tab);
}



function get_tab_info(tab_info) {
    console.log("Get tab info: ");
    console.dir(tab_info.url);

    var cur_time = Date.now();
    console.log(cur_time);
}


const sleep = (milliseconds) => {
    console.log("Sleep for " + milliseconds);
    return new Promise(resolve => setTimeout(resolve, milliseconds))
  }


async function getCPUInfo() {
    for (var idx = 0; idx < 5; idx++) {
        console.log("In loop");
        await sleep(10000);
        chrome.system.cpu.getInfo(cpu_info_handler);
    }
    // chrome.system.cpu.getInfo(function(info){
    //     console.log(JSON.stringify(info));
    //  });


}

function cpu_info_handler(cpu_info) {
    console.log("CPU Info handler: " + cpu_info);
    console.dir(cpu_info);
}

