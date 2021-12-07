* todo explain
* oh my god where do i even begin.
* javascript loop tracker https://replit.com/@mystyrust/progress-tracker#index.js 
* the 'file browser' code is there too 
* im not very good at explaining things so ill try my best

# Keeping Track of CYOA Progress
* There were a couple things I wanted to achieve with this CYOA segment 
1. the user can only open route 6 after visiting all 5 routes at least once.
2. somehow, let the user know if they've visited a route or not. (if you're like me, you'll forget instantly.)
* easy enough to accomplish with javascript - but javascript is not allowed on ao3. so our work around is to link to middleware javascript server that keeps track of which users have visited which route, and reroute you back to the fic accordingly. if you've visited all 5 routes, it will display an option for you to visit route 6 - otherwise, loop back to the beginning.
* similarly, the 'x' picture is returned conditionally. if you have not visited that route yet, it will display a 1x1 transparent pixel. if you HAVE visited the route, it will return an 'x' image displayed on top of the route - telling the reader that they've visited this route before. just a nice UX touch.