// load all students into the table as soon as the page opens
fetch("/get_students")
    .then(response => response.json())
    .then(data => {
        let table = document.getElementById("table");

        for (let s of data.students) {
            let row = table.insertRow();
            for (let i = 0; i < s.length; i++) {
                row.insertCell(i).innerText = s[i];
            }
        }
    });

function searchTable() {
    let first = document.getElementById("search_first").value.toLowerCase();
    let last = document.getElementById("search_last").value.toLowerCase();
    let age = document.getElementById("search_age").value.toLowerCase();
    let program = document.getElementById("search_program").value.toLowerCase();
    let start = document.getElementById("search_start").value.toLowerCase();
    let end = document.getElementById("search_end").value.toLowerCase();

    let rows = document.getElementById("table").rows;

    for (let i = 1; i < rows.length; i++) {
        let cells = rows[i].cells;
        let show = true;

        if (cells[1].innerText.toLowerCase().indexOf(first) == -1) {
            show = false;
        }
        if (cells[2].innerText.toLowerCase().indexOf(last) == -1) {
            show = false;
        }
        if (cells[3].innerText.toLowerCase().indexOf(age) == -1) {
            show = false;
        }
        if (cells[4].innerText.toLowerCase().indexOf(program) == -1) {
            show = false;
        }
        if (cells[5].innerText.toLowerCase().indexOf(start) == -1) {
            show = false;
        }
        if (cells[6].innerText.toLowerCase().indexOf(end) == -1) {
            show = false;
        }

        if (show) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
}