preButton=document.getElementById("prebutton");
nextButton=document.getElementsByClassName("carousel-control-next");
console.log(nextButton);
getActivate=document.getElementsByClassName("active");
console.log(getActivate);
function Myfunction (){
getActivate=document.getElementsByClassName("active");
for(var j=0;j<nextButton.length;j++)
{
    for( var i=0 ;i< getActivate.length;i++)
    {
        if(getActivate[i].getAttribute('num')==3)
        {
            console.log(getActivate[i].getAttribute('num'));
            nextButton[j].setAttribute('disabled',true);
            return;
        }
        // nextButton[j]. disabled = false;
    }
}
};
