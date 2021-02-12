$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    M.textareaAutoResize($('#description'));
});

// function validate(){
//     if(document.getElementById('category').value == ''){
//         return 0
//     }else{
//         return 1
//     }
// }

