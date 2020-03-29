window.onload = () => {
    container = document.querySelector("#end");
    var button  = document.createElement("button");

    button.innerHTML = "Dark Mode";
    button.addEventListener("click", enableDarkMode);

    var input = document.createElement("input");
    input.type = "checkbox";
    input.id = "dark-setting";
    input.addEventListener("click", storeSettings);


    container.prepend(button, input, 'Auto apply?');

    checkSetting();

}

function checkSetting() {
	chrome.storage.local.get(['enabled'], (result) => {
		console.log(result.enabled);
		document.getElementById("dark-setting").checked = result.enabled;
		if (result.enabled) {
			enableDarkMode();
		}
	})
}

function enableDarkMode() {
	alert("Enable Dark Mode!");
	ytd_app = document.getElementsByTagName("ytd-app")[0]
	ytd_app.style.backgroundColor = "#00695c";

}


function storeSettings() {
    alert("Store settings!");
    var is_enabled = document.getElementById("dark-setting").checked;
    console.log("is enabled: " + is_enabled);

    var setting = {
	    "enabled": is_enabled
    };

    chrome.storage.local.set(setting, () => {
	    console.log("stored value: " + setting);
    })
}