const departments = document.getElementById("departmentss");
const show_button = document.getElementById("btnshow");
const Hide_button = document.getElementById("btnhide");
const btn = document.getElementById("ShowDepartments");
const hide_btn = document.getElementById("HideDepartments");

btn.onclick = function () {

    show_button.style.display = "none";

    departments.style.display = "block";
    Hide_button.style.display = "block";
    //doctors.style.displayv= "block";
};
hide_btn.onclick = function () {

    show_button.style.display = "block";

    departments.style.display = "none";
    Hide_button.style.display = "none";
    //doctors.style.displayv= "none";
};
