document.addEventListener('DOMContentLoaded', function() {

    const searchBox = document.querySelector('.js-search-box'); 
    const list = document.querySelector('.js-search-result'); 
    let searchValue = ''; 

    searchBox.addEventListener('keyup', function() {
        searchValue = searchBox.value;
        startFetch(searchValue);
    });

    const startFetch = _.debounce(function(value) {
        let url = `https://cloud.iexapis.com/stable/search/${value}?token=KEY`;
        fetchData(url);
    }, 300);  

    async function fetchData (url) {
        let response = await fetch(url);
        let json = await response.json();
        printValues(json); // Pass the data over to print values function
    }

    function printValues (json) {
        list.innerHTML = '';
        json.forEach(item => {
        list.innerHTML += `<li class="drop-down-list"><a href="https://www.christiansanchez.dev/projects/search/result/${item.symbol}">${item.symbol} - ${item.name}</a></li>`;
        });
    }
});
