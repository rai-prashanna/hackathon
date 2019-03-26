// GLOBAL CONSTANTS
const SPINNER_TIMEOUT = 4000;

// =============== first page here ======== //
const welcomeFormWrapper = document.querySelector('.welcome-form');
const spinnerWrapper = document.querySelector('.spinner');
const submitButton = document.querySelector('.login') || { addEventListener: () => {} };

submitButton.addEventListener('click', () => {
  document.getElementsByTagName('html')[0].style.background = 'white';
  [welcomeFormWrapper, spinnerWrapper].forEach((el) => el.classList.toggle('hidden'));
  setTimeout(() => {
    window.location.pathname = 'results';
  }, SPINNER_TIMEOUT);
});

// animate spinner dots
const dots = document.getElementById('moving-dots') || {};
let num = 0;
setInterval(() => {
  dots.textContent = '.'.repeat(num);
  if (num === 3) {
    num = 0;
  } else {
    num += 1;
  }
}, 200);

// ============ search results here =============== //
// handle toggle if job posting
const listItems = [...document.getElementsByClassName('single-result-wrapper')];
const extraInfos = [...document.getElementsByClassName('extras')];
listItems.forEach((el, idx) => {
  el.addEventListener('click', () => {
    extraInfos[idx].classList.toggle('collapsed');
  });
});
