const body = document.querySelector('body');

// MULTIPLE PAGES, SAME MONTH
const titles = [' ', 'Transfers', 'Checks', 'Deposits', 'Wire Transfer'];
const month = 'December';
const account = 'Trust';
const year = 2024;
// titles.forEach(title => {
//   const page = document.createElement('div');
//   page.classList.add('page');
//   page.innerHTML = `<div class="page__content"><p>ELF ${account}</span> <br /> ${year} <br /> ${month} <br /><br /><br /> ${title}</p></div>`;
//   body.appendChild(page);
// });

// MULTIPLE MONTHS, SAME PAGE
const title = 'Checks';
const all_months = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December',
];

const months = all_months;

[2017].forEach(year => {
  months.forEach(month => {
    const page = document.createElement('div');
    page.classList.add('page');
    page.innerHTML = `<div class="page__content"><p>ELF ${account}</span> <br /> ${year} <br /> ${month} <br /><br /><br />${title}</p></div>`;
    body.appendChild(page);
  });
});
