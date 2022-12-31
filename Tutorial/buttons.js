$(document).ready(function() { 

    $(".css-on").click((e) => {
        $('link[href="./fireemblem-editv2.css"]').prop('disabled', false);
        // $('link[href="../CSS/twitter_new.css"]').prop('disabled', false);
    })

    $(".css-off").click((e) => {
        $('link[href="./fireemblem-editv2.css"]').prop('disabled', true);
    })

})