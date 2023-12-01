/*
    NAME:          main.js
    AUTHOR:        Alan Davies (Lecturer Health Data Science)
    EMAIL:         alan.davies-2@manchester.ac.uk
    DATE:          18/12/2019
    INSTITUTION:   University of Manchester (FBMH)
    DESCRIPTION:   JavaScript file for initializing the JavaScript functionality.
*/

$(document).ready(function () {
    $('#searchTerm').on('input', function () {
        var searchTerm = $(this).val();

        // 发送AJAX请求，获取更新后的表格HTML
        $.ajax({
            type: 'GET',
            url: '/update-table',
            data: { searchTerm: searchTerm },
            success: function (tableHTML) {
                // 将更新后的表格HTML插入到页面中
                $('#table-container').html(tableHTML);
            }
        });
    });
});


