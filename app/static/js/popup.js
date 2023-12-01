/*
    NAME:          popup.js
    AUTHOR:        Alan Davies (Lecturer Health Data Science)
    EMAIL:         alan.davies-2@manchester.ac.uk
    DATE:          18/12/2019
    INSTITUTION:   University of Manchester (FBMH)
    DESCRIPTION:   JavaScript file for managing display of popup dialoges
*/

function Popup()
{
    var popup = new Object();
    popup.mask = document.getElementById("page-mask");
    popup.entryFormPopup = document.getElementById("creat-calc");
    popup.aboutPopup = document.getElementById("about-box");

    // display the popup mask
    popup.showMask = function()
    {
        this.mask.style.display = "block";
        $('#page-mask').height($(document).height());
    }

    //hide the popup mask
    popup.hideMask = function()
    {
        this.mask.style.display = "none";
    }

    //show the creatinine clearance calculator form dialog
    popup.showCeatCalcFormPopup = function()
    {
        this.showMask();
        this.entryFormPopup.style.display = "block";
        this.positionDialogue(this.entryFormPopup);
        //this.entryFormPopup.style.left = (($(document).width() / 2) - (this.entryFormPopup.offsetWidth / 2)) + "px";
    }

    // hide the creatinine clearance calculator form dialog
    popup.hideCeatCalcFormPopup = function()
    {
        document.querySelector('input[name="sex"]:checked').checked = false;
        document.querySelector('input[name="patients-age"]').value = '';
        document.querySelector('input[name="patients-weight"]').value = '';
        document.querySelector('input[name="patients-serum"]').value = '';
        var resultDiv = document.getElementById('result');
        if (resultDiv) {
            resultDiv.textContent = '';
        }
        this.hideMask();
        this.entryFormPopup.style.display = "none";

    }

    // show the about popup
    popup.showAboutPopup = function()
    {
        this.showMask();
        this.aboutPopup.style.display = "block";
        this.positionDialogue(this.aboutPopup);
    }

    // hide about popup
    popup.hideAboutPopup = function()
    {

        this.hideMask();
        this.aboutPopup.style.display = "none";
    }

    // position dialogue center screen
    popup.positionDialogue = function(popupBox)
    {
        popupBox.style.left = (($(document).width() / 2) - (popupBox.offsetWidth / 2)) + "px";
    }

    popup.calculateCreatinineClearance = function()
    {

    var gender = document.querySelector('input[name="sex"]:checked').value;
    var age = parseInt(document.querySelector('input[name="patients-age"]').value);
    var weight = parseInt(document.querySelector('input[name="patients-weight"]').value);
    var serumCreatinine = parseFloat(document.querySelector('input[name="patients-serum"]').value);

    if (isNaN(age) || age < 1 || age > 120) {
        alert("Please enter a valid age between 1 and 120 years.");
        return;
    }

    if (isNaN(weight) || weight < 1 || weight > 120) {
        alert("Please enter a valid weight between 1 and 120 kg.");
        return;
    }

    if (isNaN(serumCreatinine) || serumCreatinine < 1 || serumCreatinine > 120) {
        alert("Please enter a valid serum creatinine between 1 and 120 micromol/L.");
        return;
    }

    var constant = (gender === "m") ? 1.23 : 1.04;

    var creatinineClearance = ((140 - age) * weight) / (72 * serumCreatinine) * constant;

    var resultElement = document.getElementById('result');
    resultElement.innerHTML = '<p>Creatinine Clearance: ' + creatinineClearance.toFixed(2) + ' ml/min</p>';
    }

    return popup;
}