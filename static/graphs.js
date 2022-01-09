var rgbToHex = function (rgb) { 
    var hex = Number(rgb).toString(16);
    if (hex.length < 2) {
         hex = "0" + hex;
    }
    return hex;
};
function setlocations(beg,rot,id1,id2) {
    var beginnig='rotate('+beg+'deg)';
    var rotating='rotate('+rot+'deg)';
    var color2=rgbToHex(parseInt(id1+5)*1000);
    console.log(color2)
    color2='#'+color2
    document.getElementById(id1).style.transform = 'rotate('+beg+'deg)';
    document.getElementById(id2).style.transform = 'rotate('+rot+'deg)';
    document.getElementById(id2).style.backgroundColor= color2;
    console.log(beginnig,rotating,color2);
}

function setColor(id) {
    var color2=rgbToHex(parseInt(id-355)*1000);
    color2='#'+color2;
    document.getElementById(id).style.color= color2;
}

