$(document).ready(function() {
    // console.log('ready')
    var currentTarget = location.hash
    if (currentTarget)
    {
        var currentHint = "." + currentTarget.substr(1) + "-hint"
        $(currentHint).css('display', 'table')
    }
   

    $("a").click((event) => {
        var target = event.currentTarget.innerText.toLowerCase()
        // var target = $(this).attr("href");
        console.log(target)

        $(".hint").css('display', 'none')

        var currentHint = "."+ target+"-hint"
        $(currentHint).css('display', 'table')
    });

    $(".arrow-reverse").click(() => {
        window.history.back();
    }) 

    $(".arrow").click(() => {
        window.history.forward();
    }) 

    $("#submit").click((event) => {
        var pwd = $("#pwd").val();

        if (pwd == "asdf") // show view
        {
            $(".incorrect-pwd").css('visibility', 'hidden');
            $(".locked-view").css('display', 'none');
            $(".unlocked-view").css('display', 'block');
        } else {
            $(".incorrect-pwd").css('visibility', 'visible');
        }
    })
})
