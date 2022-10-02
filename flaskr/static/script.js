let btn = document.getElementById("signup");

async function onClick(){
    console.log("noBitches?")
    let url = "http://127.0.0.1:5000/signUp";
    const response = await fetch(url, {method: 'POST'});

    document.getElementById("si").style.display = "none"
}

btn.addEventListener("click", onClick);

