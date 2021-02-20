$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('.modal').modal();
    $('.datepicker').datepicker();
    $(".datepicker").datepicker({
        format: "mm/dd/yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});



