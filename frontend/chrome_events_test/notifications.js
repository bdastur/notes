function create_basic_notification() {
    console.log("Create basiic notification")
    var options = {
        type: "basic",
        title: "Basic notification",
        message: "This is a basic notification!",
        iconUrl: "icon.png"
    };

    chrome.notifications.create("simple_notification",
                                options);
}


function notificationHandler(notification_id) {
    console.log("Notification  Handler: " + notification_id);
}