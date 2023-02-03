# About
* Just the raw html and css for [tired quaranteens](https://archiveofourown.org/works/27314074/chapters/66735937), a social media themed Danny Phantom fanfic hosted on ao3. 
* AO3 friendly css. 
* Base Fic is in [Quaranteens](https://github.com/mystyrust/quaranteen/tree/master/Quaranteens) folder. OtherFics folder has some sprinkles of coding for other fics. If you've noticed reused twitter usernames, it's because I reused my twitter template (a twitter cinematic universe lmao). 
  * this is turning into some sort of monorepo, since some of the css is shared for other fic bits / tutorials
* There are some CSS experiments (some 'sucessful' some 'failed') in other folders with varying degrees of organization. That is to say, you might see 3-5 copies of the same file/s.

# Tools 
Let's see I used
* [Visual Studio Code](https://code.visualstudio.com/download) - free to download, light weight text editor from microsoft (i think?) that lets you write and organize code 
* my own account on [imgur](https://imgur.com/) for static image hosting
* [MDN](https://developer.mozilla.org/en-US/docs/Learn) / [W3Schools](https://www.w3schools.com/) to reference CSS documentation. 
  * where would i be without google and stackoverflow?
* [icons8](https://icons8.com/) for icons 
* [LunaPic](https://www11.lunapic.com/editor/) for simple photo edits (crops, bg transparency)
* [pngjoy](https://www.pngjoy.com/) and [pngwing](https://www.pngwing.com/) and a few other free sites for gimmicky png resources
* google image search for background shots from the show

# Other
* ao3 pls let us use flex boxes 
* that being said, i have like... 3-4 different versions of the amongus skin bc i started out using flexboxes, then i adapted when i realized ao3 wouldnt allow it. i dont remember which ones the used one bc its all in the mega css file
* ive triiiied to keep each gimmicks css separate and only compile it together right before updating the ao3 css, in `uploaded-to-ao3-vX.css` but theres proooobably some amount of duplication. and just to be safe, i didnt want to delete anything. 
* check out the README within the [Quaranteen/CYOA](https://github.com/mystyrust/quaranteen/tree/master/Quaranteens/CYOA) folder for more info about how it was done 

# Battle log with the html parser (2023)
* changed quaranteens ch6 and ch7 to be fully in span elements, after some changes in ao3s html parser in jan 2023 prevented a tags from being siblings with divs. (a tags would be auto enclosed with p tags, preventing the tabbing mechanic from working). now quaranteens 6v2 and 7v2 was deployed
* changed quaranteens 6v2 to just quaranteens 6 after it was discovered that enclosing the entire html in a figure tag would allow a tags to be siblings with div tags again. left 7v2 as is. saved all the html
* at this point, ill keep fighting the html parser and just keep all files that have all my different (succcessful) attempts 