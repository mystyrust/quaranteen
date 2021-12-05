$(document).ready(function() {
    $(".sidebar-item").click((event) => {
        var target = event.currentTarget.innerText.toLowerCase()
        console.log(target)
    });

    $(".arrow-reverse").click(() => {
        window.history.back();
    }) 

    $(".arrow").click(() => {
        window.history.forward();
    }) 

    $("#submit").click((event)=> {
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
