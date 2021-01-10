// function addRows(){
//     var table = document.getElementById('passenger')
//     var rowCount = table.rows.length;
//     var row = table.insertRow(rowCount);
//     var colCount = table.rows[0].cells.length;
//     for(var i = 0; i<colCount; i++){
//         var newcell = row.insertCell(i);
//         newcell.innerHTML = table.rows[1].cells[i].innerHTML;
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
    // }
// }

let passengerForm = document.querySelectorAll(".passenger-form")
let container = document.querySelector("#form-container")
let addRow = document.querySelector("#addRow")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
let formNum = passengerForm.length - 1
addRow.addEventListener('click', addForm)

// for(let i=0; i<=formNum; i++){
//     checkBox = document.querySelector(`#id_form-${i}-DELETE`,'g')
//     console.log(i)
//     // checkBox.addEventListener('click', deleteForm(i))
// } 

function addForm(e){
    e.preventDefault()
    // console.log(passengerForm)
    let newForm = passengerForm[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')
    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
    container.insertBefore(newForm, addRow)

    totalForms.setAttribute('value', `${formNum+1}`)
}

// function deleteForm(i){
//     checkBox = document.querySelector(`#id_form-${i}-DELETE`);
//     form = passengerForm[i];
//     if (checkBox.checked == true){
//         // console.log(i)
//         form.style.visibility = "hidden"
//     }
// }
    // else{
    //     form.style.display="block"
    // }
//     // if (Event.target.checked){
//     // }
// }

// var add = document.querySelector("#addRow");
// add.onclick = addRows();
// document.getElementById('addRow').onclick = function() {addRows()};
// console.log("Hi")