$(document).ready(function() {
    $(".toggle_container").hide();
    $("button.hiddeninfo").click(function(){
        $(this).toggleClass("active").next().slideToggle("fast");
        return false;
    });
});