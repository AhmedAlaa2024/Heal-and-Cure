const doctors = document.getElementById("doctorss");
const show_button = document.getElementById("btnshow");
const Hide_button = document.getElementById("btnhide");
const btn2 = document.getElementById("ShowDoctors");
const hide_btn2 = document.getElementById("HideDoctors");


btn2.onclick = function () {

    show_button.style.display = "none";
    doctors.style.display= "block";
    Hide_button.style.display = "block";

};
hide_btn2.onclick = function () {

    show_button.style.display = "block";
    Hide_button.style.display = "none";
    doctors.style.display= "none";
};