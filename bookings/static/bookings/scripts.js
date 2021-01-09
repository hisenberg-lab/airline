function addRows(){
    var table = document.getElementById('passenger')
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    var colCount = table.rows[0].cells.length;
    for(var i = 0; i<colCount; i++){
        var newcell = row.insertCell(i);
        newcell.innerHTML = table.rows[1].cells[i].innerHTML;
        // switch(newcell.childNodes[0].type) {
        //     case "text":
        //         newcell.childNodes[0].value = "";
        //         break;
        //     case "select-one":
        //         newcell.childNodes[0].selectedIndex = 0;
        //         break;
        //     case "tel":
        //         newcell.childNodes[0].value = "";
        //         break;
        // }
    }
}

function deleteRows(){
    var table = document.getElementById('passenger');
    var rowCount = table.rows.length;
    if(rowCount > 2){
        var row = table.deleteRow(rowCount-1);
        rowCount--
    }
    else{
        return
    }
}

// var add = document.querySelector("#addRow");
// add.onclick = addRows();
// document.getElementById('addRow').onclick = function() {addRows()};
// console.log("Hi")