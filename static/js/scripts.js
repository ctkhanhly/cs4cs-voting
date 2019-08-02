$('document').ready(()=> {
    console.log("in scripts.js\n");
    clickChecked = (checkedBox)=>{
        console.log("checkedBox", checkedBox);
        if(checkedBox.checked){
            //$("div > this").style.backgroundColor = '#BC8F8F';
            $(checkedBox).parent().parent().css('background-color', '#BC8F8F');
        }
    }
});
