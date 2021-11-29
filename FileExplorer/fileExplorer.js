$(document).ready(function() {
    $(".sidebar-item").click((event) => {
        // var classes = $(target.currentTarget).attr("class");
        // console.log(classes)
        var target = event.currentTarget.innerText.toLowerCase()
        console.log(target)

    });
})
