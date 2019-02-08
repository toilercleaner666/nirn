############################################################
#  Welcome to the GitHub repository for Nirn Universalis!  #
############################################################

Nirn Universalis repository guidelines:
	Structure:
	- Any mod content should be in the NirnUniversalis folder
	- The folder structure should resemble the structure in the vanilla installation (Steam library -> show local files)
	- If you are adding events, decisions, scripted effects, localisations or similar things that do not depend on file
		names, add them on to existing files that match the theme closely. 
		If there is no close match, put them in a new file.
	
	Code:
	- Code files should be indented with tabs, set GitHub to 'Tabs' in the top right corner for code files
		The usual indent size is 4, but you can choose any size you want as long as you use tabs.
		YAML files (.yml) are exempt from this, they require precise whitespace formatting with single spaces.
	
	Git:
	- Commits should have a title that says what the commit is about, and a comment that outlines what it does
	- When writing the title, think of it like asking "If this commit is done, it will [...]"
		An example would be 'add provinces to Skyrim superregion', or 'weaken army professionalism effects'
		This results in clear, concise and uniform notes, keeping them easily readable in what will be a long list
	- When writing the comment, keep single lines below 72 characters. Use the preview function to check the format.
	

################################
Git introduction for new people:
################################

	Github is a great tool to work on a single project collaboratively, even if the work areas overlap.
	Git keeps track of all changes done, everything can be reverted and changed at any time, and collaborative projects
	can be brought together peacefully.
	
	While working with GitHub over the website is doable, the proper use of Git will require a proper program.
	For some advanced cases, it might even be necessary to use the console.
	
	Download GitKraken (a decent Git managing tool) here: https://www.gitkraken.com/git-client
	
	Download Git for console here, if the need arises: https://git-scm.com/downloads
	
	There are many alternatives to GitKraken, though I do not have experiences with any of them. Many modern code 
	processing tools have some form of Git support.
	
	After setting up an account in GitKraken, click on "Open a project" select "clone" and "GitHub".
	Connect your GitHub account and confirm the link in the browser. You should now see the repository listed in
	GitKraken, click on it and give it a suitable location at "Where to clone to" on your computer (e.g. C:/, or
	C:/Users/[username]) and confirm to download the repository to your computer.
	
	You should now see the commit timeline in the middle, with the latest changes being at the top. Different colours
	indicate different repository branches, and every branch has a marker to show at which point in the timeline it is
	currently situated. You can click on any commit to see what exactly it changes on the right side.
	
	On the left side, there will be a tab named "LOCAL", containing the branch "master". Right-click on master and select
	"create branch here", give it a name containing your username (or a designated use for the new branch), and confirm.
	There should now be a new marker with a new colour on the timeline, next to the marker for "master". Right-click on
	your new branch and click "push" to copy this new branch on to the online repository as well - when GitKraken asks you
	which origin branch this new local branch should be connected to, just click accept to create a new online branch with
	the same name as the local one.
	
	You can switch between local branches by selecting "checkout" or double-clicking, this edits your local files to
	resemble the state of the specified branch. If you checkout branches from the REMOTE part, they will automatically be
	copied into the local area. 
	
	Make sure that you have checked out your own, new, branch. You can now make changes in the files directly, right where
	you set the repository to be cloned to. Much more convenient than editing stuff online. GitKraken will notice anything
	that you have done, the 'empty' commit at the top shows the changes.
	
	Once you've done some changes, click on "stage all" on the right to confirm them, or stage changed files individually.
	Once you're done staging changes, click on "commit" to finalise your changes and add them to your project timeline.
	While committing, do not forget to write a proper title and short description in the bottom right corner.
	
	You do not have to be done with your changes before committing - in fact, committing often is better than rarely.
	Commits define the points to which you can return to undo or redo something, if they are too broad, you'll have to go
	in and edit files specifically rather than simply reverting a commit.
	
	Once you've done a few commits and are satisfied with your work, left-click on your branch on the left and select
	"push" to send the commits off to the online repository.
	
	And once your branch has done its job and is fully playable, start a pull request from your online branch to the
	master branch. The one in charge of the repository will then merge the two branches together, and master will contain
	everything that you have made in the branch.
	
####	
More to come
####
Feel free to edit this file along with the rest of the mod!
