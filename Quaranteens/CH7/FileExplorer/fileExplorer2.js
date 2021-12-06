$(document).ready(function() {
    // console.log('ready')
    // var currentTarget = location.hash
    // if (currentTarget)
    // {
    //     var currentHint = "." + currentTarget.substr(1) + "-hint"
    //     $(currentHint).css('display', 'table')
    // }

    var fileBrowserHistory = [];
    var historyIndex = 0;

    const navigateTo = (target) => {
        $(".hint").css('display', 'none')
        $(".tab").css('display', 'none')

        var currentHint = "."+ target+"-hint"
        var currentTarget = "."+target

        $(currentHint).css('display', 'table') // or display block?
        $(currentTarget).css('display', 'block')
    }

    $("a").click((event) => {
        // var target = event.currentTarget.innerText.toLowerCase()
        var target = event.currentTarget.classList[0];
        // var target = $(this).attr("href");
        console.log(target)

        // $(".hint").css('display', 'none')
        // $(".tab").css('display', 'none')

        // var currentHint = "."+ target+"-hint"
        // var currentTarget = "."+target

        // $(currentHint).css('display', 'table') // or display block?
        // $(currentTarget).css('display', 'block')
        
        navigateTo(target)
        fileBrowserHistory.push(target);
        historyIndex++
    });


    $(".arrow-reverse").click(() => {
        // window.history.back();
        // historyIndex--
        historyIndex--
        var target = fileBrowserHistory[historyIndex]
        navigateTo(target)
    }) 

    $(".arrow").click(() => {
        // window.history.forward();
        if (historyIndex + 1 < fileBrowserHistory.length)
        {
            historyIndex++
            var target = fileBrowserHistory[historyIndex]
            navigateTo(target)
        }
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
