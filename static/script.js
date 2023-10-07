// JavaScript to handle tab content visibility
function showTab(tabId) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(tab => {
        tab.style.display = 'none';
    });

    // Show the selected tab content
    const selectedTab = document.getElementById(tabId);
    selectedTab.style.display = 'block';
}