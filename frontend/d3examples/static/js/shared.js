/*
alert("Shared js");
var backdrop = document.querySelector('.modal');
console.log(backdrop);
console.dir(backdrop);
backdrop.style.display = "block";
*/

var modal = document.querySelector(".modal");
var modalNoButton = document.querySelector(".modal__action--negative");
var toggleButtton = document.querySelector(".toggle-button");
var mobileNav = document.querySelector(".mobile-nav");

var selectPlanButton = document.querySelectorAll('.action-button');
console.dir(selectPlanButton);
console.dir(modalNoButton);

for (var i = 0; i < selectPlanButton.length; i++) {
	selectPlanButton[i].addEventListener('click', function() {
		modal.style.display = "block";
	});
}


modalNoButton.addEventListener('click', closeModal);

function closeModal() {
	modal.style.display = "none";
};


toggleButtton.addEventListener('click', openNav);

function openNav() {
	if (mobileNav.style.display == "none") {
		mobileNav.style.display = "block"
	} else {
		mobileNav.style.display = "none";
	}
}