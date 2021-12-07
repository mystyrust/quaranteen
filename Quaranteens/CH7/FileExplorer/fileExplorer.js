$(document).ready(function() {
    // console.log('ready')
    $(".hint").css('display', 'none')
    var currentTarget = location.hash

    var fileBrowserHistory = []
    var historyIndex = 0

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
        fileBrowserHistory[historyIndex] = target;
        historyIndex++
    });

    $(".arrow-reverse").click(() => {
        window.history.back();
    }) 

    $(".arrow").click(() => {
        window.history.forward();
    }) 

    $("#submit").click((event) => {
        var pwd = $("#pwd").val();

        if (pwd == "iLov3Maddie") // show view
        {
            $(".incorrect-pwd").css('visibility', 'hidden');
            $(".locked-view").css('display', 'none');
            $(".unlocked-view").css('display', 'block');

            $(".locked-hint").remove();

            $(".documents-hint-unlocked")
                .removeClass("documents-hint-unlocked")
                .addClass("documents-hint")
                .css('display', 'table');
            
        } else {
            $(".incorrect-pwd").css('visibility', 'visible');
        }
    })

    $(".download-final").click(() => {
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
            // hide all previous hints
            $(".research-downloaded").removeClass("hint").css('display', 'table');
            $(".hint:not(.research-downloaded)").remove();
        }, 2000)
    })

    $(".download-weapons").click(() => {
        console.log('clicked download')
        // downloading
        $(".download-all").toggle()
        $(".weapons .document-list").toggle()
        $(".loader").toggle()

        // then, download complete
        setTimeout(() => { 
            $(".loader-complete").toggle()
        }, 1000)

        setTimeout(() => { 
            $(".download-all").toggle()
            $(".weapons .document-list").toggle()
            $(".loader").toggle()
            $(".loader-complete").toggle()

            // then show new danny hint afterwards too

            $(".weapons-hint").remove();
            $(".weapons-hint-downloaded ")
                .removeClass("weapons-hint-downloaded ")
                .addClass("weapons-hint")
                .css('display', 'table');
            // hide all previous hints
            // $(".research-downloaded").removeClass("hint").css('display', 'table');
            // $(".hint:not(.research-downloaded)").remove();
        }, 2000)
    })

})
