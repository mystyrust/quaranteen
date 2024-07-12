$(document).ready(function() { 

    $(".css-on").click((e) => {
        // $('link[href="./ecto-implosion.css"]').prop('disabled', false);
        $('link[href="./mlb-dp.css"]').prop('disabled', false);
        // $('link[href="../CSS/twitter_new.css"]').prop('disabled', false);
    })

    $(".css-off").click((e) => {
        $('link[href="./mlb-dp.css"]').prop('disabled', true);
    })

})