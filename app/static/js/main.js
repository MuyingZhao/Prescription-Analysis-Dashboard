/*
    NAME:          main.js
    AUTHOR:        Alan Davies (Lecturer Health Data Science)
    EMAIL:         alan.davies-2@manchester.ac.uk
    DATE:          18/12/2019
    INSTITUTION:   University of Manchester (FBMH)
    DESCRIPTION:   JavaScript file for initializing the JavaScript functionality.
*/

var popup = null;
var barChart = null;
var search = require('./search'); // Adjust the path based on your file structure

// initialisation function
function initializeMain()
{
    popup = Popup();
    barChart = BarChart();
    search();
}
