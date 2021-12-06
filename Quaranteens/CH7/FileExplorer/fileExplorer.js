$(document).ready(function() {
    // console.log('ready')
    $(".hint").css('display', 'none')
    var currentTarget = location.hash
    // var fileBrowserHistory = []

    if (currentTarget)
    {
        var currentHint = "." + currentTarget.substr(1) + "-hint"
        $(currentHint).css('display', 'table')
    }
   
    $("a").click((event) => {
        var target = event.currentTarget.hash.substr(1)
        // var target = event.currentTarget.name;
        // var target = $(this).attr("href");
        console.log(target)

        $(".hint").css('display', 'none')

        var currentHint = "."+ target+"-hint"
        $(currentHint).css('display', 'table')

        // location.replace("#" + target)
        // fileBrowserHistory[historyIndex] = target;
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

            $(".unlocked-hint").css('display', 'table');
            $(".locked-hint").css('display', 'none');
            
        } else {
            $(".incorrect-pwd").css('visibility', 'visible');
        }
    })

    $(".download-all").click(() => {
        console.log('clicked download')
        // downloading
        $(".download-all").toggle()
        $(".research .document-list").toggle()
        $(".loader").toggle()

        // then, download complete
        setTimeout(() => { 
            $(".loader-complete").toggle()
        }, 1000)

        setTimeout(() => { 
            $(".download-all").toggle()
            $(".research .document-list").toggle()
            $(".loader").toggle()
            $(".loader-complete").toggle()
            // then show new danny hint afterwards too
        }, 2000)
    })

})
