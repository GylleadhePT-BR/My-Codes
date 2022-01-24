function showModal(){
    var element = document.getElementById("modal");
    element.classList.add("show-modal");
    document.documentElement.style.overflow='hidden';
    document.body.scroll="no";
}
function hideModal(){
    var element = document.getElementById("modal");
    element.classList.remove("show-modal");
    document.documentElement.style.overflow='auto';
    document.body.scroll="yes";
}

const cart = document.getElementById("cart")
const bar = document.getElementById("bar");
const nav = document.getElementById("navbar")
const bag = document.getElementById("lg-bag")
var close = document.getElementById("close")
if(bar){
    bar.addEventListener('click',() =>{
        nav.classList.add('active')
        bar.style.visibility="hidden";
        cart.style.visibility="hidden";
    
    })
}
if(close){
    close.addEventListener('click',() =>{
        nav.classList.remove('active')
        bar.style.visibility="visible"
        cart.style.visibility="visible"
    })
}