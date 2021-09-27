function tweet() {
    
    // todos
    // preview profile pic
    // create profile object
    // dynamically add to array of profile objects
    // When loading mockup, extract unique list of all 'profiles'
    // make date inclusion optional? 
    // edit individual tweets

    // get all inputs
    // create tweet object? to access indexing? 
    // get tweet objects from html inputs?
    

    // turn into a "profile" thats easily swapable? 
    // easier tweeting? 
    var picUrl = $("#pic").val(); // preview?
    var username = $("#username").val();
    var handle = $("#handle").val();


    var tweetMsg = $("#tweet").val(); // auto format hastags and @s
    var date = $("#date").val(); // format 
    // var time = $("#date").val(); // format 
    var likes = $("#likes").val();
    var retweets = $("#retweets").val();
    var replys = $("#replys").val();
    var accountStatus = $('input[name=accountStatus]:checked').val();
    var replyIndex = false;

    // logic -> transform values / compute html 

    var accountStatusHtml = ""; // verified or private add icons?
    if (accountStatus === "verified") { // enum? 
        accountStatusHtml = `<img class="twIcon" src="http://imgur.com/eVQzzhT.png">`;
    } else if (accountStatus === "private") {
        accountStatusHtml = `<img class="twIcon" src="https://i.imgur.com/L76idO6.png">`;
    } 

    var twRespond = ""; // add indent if this is reply tweet
    if (replyIndex) {
        twRespond = "twRespond";
    }

    // add 'hyperlinks' to @s and #s in tweetMsg 
    // error prone if spacing is not standard
    var tweetArray = tweetMsg.split(" ");
    $.each(tweetArray, function(index, value) {
        if (value.startsWith("@") || value.startsWith("#")) {
            tweetArray[index] = `<span class='twLink'>${tweetArray[index]}</span>`
        }
    });
    tweetMsg = tweetArray.join(" ");

    //format timestamp

    var html = 
    `<div class="tw ${twRespond}">
        <p class="twBody">

            <span>
                <img class="twAvatar" src="https://i.imgur.com/yagB5ob.png">
                <span class="twUser">
                    <span class="twUserName">${handle}
                        ${accountStatusHtml}
                    </span>
                    <br>
                    <span class="twUserHandle">@${username}</span>
                </span>
            
                <img class="twFollow" src="http://imgur.com/p6lbN22.png">
                <br>
            </span>
            
            <span class="twText">
                ${tweetMsg}
            </span>
            
            <span class="twTimeStamp"> 3:42 PM - 5 Sept 2018 </span>
            
            <span>
                <img class="twReplyIcon" src="http://imgur.com/9dwkilY.png"> 53
                <span class="twRetweet"> 
                    <img class="twRetweetIcon" src="http://imgur.com/ToOoCJz.png"> 100
                </span>
            
                <span class ="twLike">
                <img class="twHeartIcon" src="http://imgur.com/67stmhs.png"> 87
                </span>
            </span>
            
        </p>
    </div>
    `;

    var srcCode = $("#story");
    srcCode.val(srcCode.val() + html);

    html = `<div class="twContainer"> 
    ` + html + `
        <button type="button" class = "edit" onclick="editSingleTweet()">Edit Tweet</button>
        </div>
    `;

    // todo add other btns

    $("#mockupOutput").append(html);

    // srcCode.css('overflow', 'hidden').autogrow();
    // add to copypaste pane

    // todo fix this -> delete single tweet
    // $(":button.edit").click(function() {
    //     var tweetContainer = $(this).parent();
    //     var tweetHtml = tweetContainer.find(".tw").html();
    //     var copyPastePane = $("#story").val();
    //     copyPastePane = copyPastePane.replace(tweetHtml, "\n");
    //     $("#story").val(copyPastePane);
    //     tweetContainer.remove();
    // });
}

function clearAll() {
    // empty everything
    $("#mockupOutput").empty()
    $("#story").val("");
}

function restoreProgress() {
    // take html from copypaste pane and replace it in the mockup
    var srcCode = $("#story").val();
    $("#mockupOutput").empty()
    $("#mockupOutput").append(srcCode);
}

// TODO
function createProfile() {
    // turn into a "profile" thats easily swapable? 
    // easier tweeting? 
    var picUrl = $("#pic").val(); // preview?
    var username = $("#username").val();
    var handle = $("#handle").val();

    // create 'profile' object?
}

function editSingleTweet() {
    // pop up text box (?)
    // take input values
    // update mock up 
    // update copypaste pane
}

function deleteSingleTweet() {
    // on button click
    // find prev .tw
    // remove it from copy paste pane
    // clear
    // 
}

function addSingleTweet() {

}

function loadProfile() {
    // select profile object and populate form
}