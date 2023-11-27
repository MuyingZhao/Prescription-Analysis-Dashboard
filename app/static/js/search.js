/*
    NAME:          main.js
    AUTHOR:        Alan Davies (Lecturer Health Data Science)
    EMAIL:         alan.davies-2@manchester.ac.uk
    DATE:          18/12/2019
    INSTITUTION:   University of Manchester (FBMH)
    DESCRIPTION:   JavaScript file for initializing the JavaScript functionality.
*/

function Search() {

    var searchTerm = document.getElementById('searchInput').value;

    // Make an AJAX request to the backend with the search term
    // Update the table with the search results
    // Example using Fetch API
    fetch('/search_drug?term=' + searchTerm)
        .then(response => response.json())
        .then(data => updateTable(data));
}

function UpdateTable(data) {
    var table = document.getElementById('drugTable');
    var tbody = table.getElementsByTagName('tbody')[0];

    // Clear existing rows
    tbody.innerHTML = '';

    // Add new rows based on the search results
    data.forEach(drug => {
        var row = tbody.insertRow();
        var bnfCodeCell = row.insertCell(0);
        var bnfNameCell = row.insertCell(1);
        var itemsCell = row.insertCell(2);
        var nicCell = row.insertCell(3);
        var actCostCell = row.insertCell(4);
        var quantityCell = row.insertCell(5);

        bnfCodeCell.innerHTML = drug.BNF_code;
        bnfNameCell.innerHTML = drug.BNF_name;
        itemsCell.innerHTML = drug.items;
        nicCell.innerHTML = drug.NIC;
        actCostCell.innerHTML = drug.ACT_cost;
        quantityCell.innerHTML = drug.quantity;

        // Add more cells as needed based on your data model
    });
}

module.exports = search;