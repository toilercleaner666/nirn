#  Welcome to the GitHub repository for Nirn Universalis!

## About our mod: 
Nirn Universalis is a Work In Progress mod for Europa Universalis IV, based on the Elder Scrolls world of Nirn, and its map, mechanics, and history.

Current Progress: We have completed the Map and definition files, and are working on province names, as well as dividing up the world into areas and regions. We have also completed cultures, and started work on religions, advisor portraits, and colormaps.

We have no predictable date for release, however, work on the mod continues and we have a team of 4 developers and 3 artists making sure the mod reaches the steam workshop as soon as is possible. Since work on the mod is during our own free time, we can afford to give no gaurentees regarding time.

Join our discord server if you have any further questions about the direction the mod is taking, progress in specific areas, or suggestions. https://discord.gg/Spsh9pA

We post regular updates on our subreddit: https://www.reddit.com/r/nirnuniversallis/

## Current mod status:
### Completed:
+ Fully Functional Map
+ Trade Nodes (no connections)
### In Progress:
+ Map:
    1. Strait Crossings
    2. Water Map
    3. Province Positions (Manually adjusted)
    4. Trade Node Connections
+ Political Map and Countries
+ Cultures
+ Religions
+ Advisor Portraits
+ Localization

## Nirn Universalis contribution guidelines:

Feel free to contribute to our mod! Read on if you know how GitHub works, otherwise go check out the introduction section below this first.
If you want to contribute, please either join our discord server and contribute through there, or alternatively make a fork of the repository, make your changes, and send us a merge request so we can evaluate your changes and make sure they fit in with our goal for the mod.

Some guidelines:

Commit messages should be relevant to the commit, and it should be easy to understand from the message what issue it refers to (referenced through the issue number), what problem it fixes, or what feature (events, decisions, etc) it adds. We highly recommend few and frequent commits, with every working batch of code committed individually. If you want to commit a lot of work in bulk, we would also ask you to include a detailed description with the message telling us more about what you did.

All mod content should be within the NirnUniversalis folder, and should mimic the placement of files in the vanilla installation directory. Files such as paint.net files for the map, non-eu4 scripts to make file writing less tedious, etc. or any other useful file that does not belong in the game files themselves, should be placed in the main directory.

When adding events, decisions, scripted effects, localisations or similar things that do not depend on file names, add them on to existing files that match the theme closely. If there is no close match, put them in a new file. This keeps the mod organized.
Please indent all code, and comment everything you write (a # symbol starts a line comment in the game files)

## Suggestions / Bug reports:

For any suggestions you want to make, or bugs you want to report, please open up a new issue. Write a detailed and relevant issue, with steps to reproduce if it's a bug, or details about the suggested feature if itss a suggestion. We are open to all suggestions for the mod, from potential events, to National Ideas, to disasters; but we would request all suggestions you make are true to the lore (and provide relevant wiki links wherever possible)
	

## GitHub introduction for new people:

Github is a great tool to work on a single project collaboratively, even if the work areas overlap. Git keeps track of all changes done, everything can be reverted and changed at any time, and collaborative projects can be brought together peacefully. While working with GitHub over the website is doable, the proper use of Git will require a proper program. 
	
Download GitKraken (a decent Git managing tool) here: https://www.gitkraken.com/git-client
	
Download Git for console here, if the need arises: https://git-scm.com/downloads
	
There are many alternatives to GitKraken, though I do not have experiences with any of them. Many modern code  processing tools have some form of Git support, though most of these wont be applicable to the EU4 game files.

### Using GitKraken:
	
After setting up an account in GitKraken, click on "Open a project" select "clone" and "GitHub". Connect your GitHub account and confirm the link in the browser. You should now see the repository listed in GitKraken, click on it and give it a suitable location at "Where to clone to" on your computer (e.g. C:/, or C:/Users/[username]) and confirm to download the repository to your computer.
	
You should now see the commit timeline in the middle, with the latest changes being at the top. Different colours indicate different repository branches, and every branch has a marker to show at which point in the timeline it is currently situated. You can click on any commit to see what exactly it changes on the right side.
	
On the left side, there will be a tab named "LOCAL", containing the branch "master". Right-click on master and select "create branch here", give it a name containing your username (or a designated use for the new branch), and confirm. There should now be a new marker with a new colour on the timeline, next to the marker for "master". Right-click on your new branch and click "push" to copy this new branch on to the online repository as well - when GitKraken asks you which origin branch this new local branch should be connected to, just click accept to create a new online branch with the same name as the local one.
	
You can switch between local branches by selecting "checkout" or double-clicking, this edits your local files to resemble the state of the specified branch. If you checkout branches from the REMOTE part, they will automatically be copied into the local area. 
	
Make sure that you have checked out your own, new, branch. You can now make changes in the files directly, right where you set the repository to be cloned to. Much more convenient than editing stuff online. GitKraken will notice anything that you have done, the 'empty' commit at the top shows the changes.
	
Once you've done some changes, click on "stage all" on the right to confirm them, or stage changed files individually. Once you're done staging changes, click on "commit" to finalise your changes and add them to your project timeline. While committing, do not forget to write a proper title and short description in the bottom right corner.
	
You do not have to be done with your changes before committing - in fact, committing often is better than rarely. Commits define the points to which you can return to undo or redo something, if they are too broad, you'll have to go in and edit files specifically rather than simply reverting a commit.
	
Once you've done a few commits and are satisfied with your work, left-click on your branch on the left and select "push" to send the commits off to the online repository.

And once your branch has done its job and is fully playable, start a pull request from your online branch to the master branch. The one in charge of the repository will then merge the two branches together, and master will contain everything that you have made in the branch.
(Of course, we would much prefer it if you make a fork of the repository and edit in that, then send a merge request for your code back to the main repository, and all of that can be easily done through the browser window; however, using a branch is much easier if you are just starting off learning Git)
	
You can always just use GitHub Desktop, which has a similar UI, or alternatively a terminal interface (or Git-Bash on windows) to really make your life easier if you know how to use it.

## Useful Scripts / Applications:
These are a list of external programs we have used while working on this mod.

Paint.net (image editor): https://www.getpaint.net
EU4 Area File Program (made by Anurag-Shah, used to generate formatted files): https://github.com/Anurag-Shah/EU4AreaFileProgram
