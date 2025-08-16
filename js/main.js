// --- Product Detail Page Tabs ---
const tabs = document.querySelectorAll('.tab-link');
const tabContents = document.querySelectorAll('.tab-content');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = document.querySelector('#' + tab.dataset.tab);

        // Remove active class from all tabs and content
        tabs.forEach(t => t.classList.remove('active'));
        tabContents.forEach(tc => tc.classList.remove('active'));

        // Add active class to clicked tab and corresponding content
        tab.classList.add('active');
        target.classList.add('active');
    });
});