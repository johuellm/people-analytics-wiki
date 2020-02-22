$(document).ready(function () {

    if(sessionStorage.getItem("sessionKey") == "true") {
        var table = $('#dtBasicExample').DataTable({});
        var invisibleCols = sessionStorage.getItem("invisibleCols").split(',').map(function(item) {
            return parseInt(item, 10);
        });;
        var visibleCols = sessionStorage.getItem("visibleCols").split(',').map(function(item) {
            return parseInt(item, 10);
        });;;
    } else {
        var table = $('#dtBasicExample').DataTable({});
        var invisibleCols = [1, 3, 11, 13, 14, 15, 16];
        var visibleCols = [0, 2, 4, 5, 6, 7, 8, 9, 10, 12];
        sessionStorage.setItem("sessionKey", "true");
        sessionStorage.setItem("invisibleCols", invisibleCols);
        sessionStorage.setItem("visibleCols", visibleCols);
    }

    var defaultCols = [0, 2, 4, 5, 6, 7, 8, 9, 10, 12];

    /*Workaround for the location of the "toggle-columns"-dropdown*/
    var itm = document.getElementById("toggle-dropdown");
    var cln = itm.cloneNode(true);
    itm.parentNode.removeChild(itm);
    var wrapper = document.getElementById("dtBasicExample_wrapper");
    wrapper.insertBefore(cln, wrapper.childNodes[0]);

    
    $('.dataTables_length').addClass('bs-select');
    $('a.toggle-vis').on( 'click', function (e) {
        e.preventDefault();

        /*show all function*/
        if($(this).attr('data-column')==999) {
            if(invisibleCols.length>0) {
                for (var item in invisibleCols) {
                    var columnToShow = table.column(invisibleCols[item]);
                    columnToShow.visible( ! columnToShow.visible());
                    visibleCols.push(invisibleCols[item]);
                    document.getElementById("column-" + invisibleCols[item]).innerHTML = "X";
                }
                invisibleCols.splice(0, invisibleCols.length);
            }
        }

        /*hide all function*/
        else if($(this).attr('data-column')==998) {
            if(visibleCols.length>0) {
                for (var item in visibleCols) {
                    var columnToHide = table.column(visibleCols[item]);
                    columnToHide.visible( ! columnToHide.visible());
                    invisibleCols.push(visibleCols[item]);
                    document.getElementById("column-" + visibleCols[item]).innerHTML = "";
                }
                visibleCols.splice(0, visibleCols.length);
            }
        }
        /*show default function*/
        else if ($(this).attr('data-column')==997){
            for(var i=0; i<=16;i++) {
                if(defaultCols.indexOf(i)==-1 && invisibleCols.indexOf(i) == -1) {
                    var hideCol = table.column(i);
                    hideCol.visible( ! hideCol.visible());
                    invisibleCols.push(i);
                    document.getElementById("column-" + i).innerHTML = "";
                    visibleCols.splice(visibleCols.indexOf(i), 1)
                } else if(defaultCols.indexOf(i)>=0 && visibleCols.indexOf(i)==-1) {
                    var showCol = table.column(i);
                    showCol.visible( ! showCol.visible());
                    visibleCols.push(i);
                    document.getElementById("column-" + i).innerHTML = "X";
                    invisibleCols.splice(invisibleCols.indexOf(i), 1)
                }
            }
        }
        else {
            var column = table.column( $(this).attr('data-column') );
            column.visible( ! column.visible() );
            var elementIdString =  parseInt($(this).attr('data-column'));
            var text = "column-"
            var finalId = text + elementIdString;
            if(column.visible()==true) {
                document.getElementById(finalId).innerHTML = "X";
                visibleCols.push(elementIdString);
                invisibleCols.splice(invisibleCols.indexOf(elementIdString), 1);
            } else {
                document.getElementById(finalId).innerHTML = "";
                invisibleCols.push(elementIdString);
                visibleCols.splice(visibleCols.indexOf(elementIdString),1);
            }
        }
        sessionStorage.setItem("table", table);
        sessionStorage.setItem("invisibleCols", invisibleCols);
        sessionStorage.setItem("visibleCols", visibleCols);
    });

    /*set initial checks*/
        for(var i = 0;i<=16;i++) {
            var fieldId = "column-" + i;
            document.getElementById(fieldId).innerHTML = "X";
        }

    /*removes non-default columns that are definded in the param invisibleCols
    remove checks*/
        for(var item in invisibleCols) {
            var columnToHide = table.column(invisibleCols[item]);
            document.getElementById("column-"+invisibleCols[item]).innerHTML = "";
            columnToHide.visible( ! columnToHide.visible());
            sessionStorage.setItem("table", table);
            sessionStorage.setItem("invisibleCols", invisibleCols);
            sessionStorage.setItem("visibleCols", visibleCols);
            }
    });


window.onload = function(){
        $.get("sidebar.html", function(data){
            $("#include").html(data);
        })
    }

function includeHTML() {
    var z, i, elmnt, file, xhttp;
    /* Loop through a collection of all HTML elements: */
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
        elmnt = z[i];
        /*search for elements with a certain atrribute:*/
        file = elmnt.getAttribute("w3-include-html");
        if (file) {
        /* Make an HTTP request using the attribute value as the file name: */
        xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4) {
            if (this.status == 200) {elmnt.innerHTML = this.responseText;}
            if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
            /* Remove the attribute, and call this function once more: */
            elmnt.removeAttribute("w3-include-html");
            includeHTML();
            }
        }
        xhttp.open("GET", file, true);
        xhttp.send();
        /* Exit the function: */
        return;
        }
    }
    }

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
      })

function generateValue(){

      'apple'.split('').forEach(function (c) {
        console.log(c + ': ' + c.charCodeAt(0));
      });}

