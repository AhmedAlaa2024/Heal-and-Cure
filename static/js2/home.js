
function dropdownmenu()
{
    var x = document.getElementById("dropdownclick");
    if(x.className === "topnav")
       {
            x.className += " responsive";
       }
    else
        {
            x.className = "topnav";
        }
}

function login(isLoggedIn)
{
    if(isLoggedIn)
    {
        var x = document.getElementById("login");
        var y = document.getElementById("Sign_up");
        x.remove();
        y.remove();
    }
    else
    {

    }
    
}