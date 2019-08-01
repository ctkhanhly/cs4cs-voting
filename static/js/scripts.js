// console.log("in scripts.js\n");
// var clickChecked = (checkedBox)=>{
//         console.log("checkedBox", checkedBox);
//         if(checkedBox.checked){
//             // $("div > this").style.backgroundColor = '#BC8F8F';
//             $(this).parent().css({'background-color': '#BC8F8F';});
//         }
//     }
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
// function myFunction(x, _this) {
//     x.style.backgroundColor = _this.checked ? '#0000FF' : '#FF0000';
// }