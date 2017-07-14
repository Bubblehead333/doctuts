'''GIT Tutorial Document

GIT is a Version Control system. It takes saves of the same file and
commits them to an online repository where it stashes each version of 
the file. This is useful if a new version of the code breaks something
and the code bases needs to be reverted to a previous save.

github.com 	- Is the free to use version of GIT VCS
stash.com  	- Is the business use of GIT. This has recently been updated 
			- to bitbucket.
			

Contents

1. Install
----------

	1.1 Installing GIT on Raspberry Pi
	1.2 Creating a Global User Account


2. Creating a Repository
------------------------
	
	2.1 Creating a local repository
	2.2 Adding your files to GIT
	
	
	
	
3.	Committing and Pushing
--------------------------

	3.1 Linking your Account
	3.2 Making a Commit
	3.2 Pushing your Commit
	
	

4. 	Pulling
-----------
	
	4.1 Pulling Requests
	
	
=======
4.	Cloning or downloading a repository


1. Install
----------



	1.1 Install GIT on Raspberry Pi
	-------------------------------
	
	
To install GIT on a Raspberry Pi:


	sudo apt install git



	1.2 Creating a Global User Account
	----------------------------------
	
	
	git config --global user.name "Your Name"
	git config --global user.email "your@email"


Will create a username and email for your account.

git config --global core.editor nano

This tells GIT which text editor you will use by default. In this 
instance we are using nano.



2. Creating a Repository
------------------------


	2.1 Creating a local repository
	-------------------------------
	

	
It is first wise to create a directory in which your files will be 
stored in. For short you can use:


	mkdir code_directory
	
	
This will create a folder in home/pi called 'code_directory'
To change directory, or move into the newly created folder:


	cd code_directory
	
	
With ever new repository it is good practice to create a README file.
To do this on command line use:


	nano README.md
	
	
This will open up the text editor nano and create a file called 
README.md. You can then type anything you want within the field. To
save your work press Ctrl+X to save, and the Y to save changes. Press
enter to accept the file name. 

You will then need to initialise your new repo.


	git init
	
	
Creates files needed for github, stash or bitbucket to recognise you 
directory as a GIT repo. 


	
	2.2 Adding your files to GIT
	---------------------------------
	
To add your new file, use:

	
	git add README.md
	

You can also use the following to add every file in your current 
directory:


	git add --all
	
	
If you wish to see which files have been stage to commit, you can use:


	git status
	
	
You can also monitor the changes within the files that have been added.


	git diff
	
	
Shows the differences of the files that have not yet been staged.


	git diff --staged
	
	
Shows the differences of files that have been staged to the last file
version.	



3. Committing and Pushing
-------------------------


	3.1 Linking your Account
	------------------------

	
The file README.md is now staged. It has been COMMITTED. This means that
changes have been saved but not necessarily PUSHED up to the online
repository.

To do this you need to link your online account to your local repo.
Create an account at github, and select the tab where it says to create
a new repository.

Upon creating a new repository, a page with a clear tutorial will show.

In this instance use the section titled 'Push an existing repository 
from the command line'.
Change directory into where your repo is stored locally, then follow
the instructions. (I am going to just copy and paste their tutorial)

	git remote add origin https://github.com/Bubblehead333/repo_name.git
	
This points the repo to the online URL to where the files will be 
stored. 

	
	
	3.2 Making a Commit
	-------------------
	
To finally commit:


	git commit -am 'add README.md'
	
	
This commits everything that has been added or staged, and adds a 
comments 'add README.md' to the commit.

Committing a file is almost like saving your file LOCALLY. You can 
uncommit your file so that when you push, that file is not included.
To do this you can use:


	git reset 'file_name'
	



	3.3 Pushing your Commit
	------------------------
	
	git push -u origin master
	
This will PUSH the COMMITTed files up to the online repo. To finish
the PUSH you will have to fill in your online credentials. 

It is wise then to check whether your files have successfully uploaded.



4. Pulling, Cloning or downloading a repository
-----------------------------------------------
	
	4.1 Cloning a Repository
	--------------------------------------
	
To download a repo onto your local, go to github.com and log into your
account. Then navigate to the repo you wish to download, and click the
'Clone or download' button. This will give you an SSH URL so you can 
download the repo via GIT. You can also use HTTPS protocol though this
is less secure.
When you have the URL you wish to use, and you are in the directory you 
want, you can the use the following:


	git clone [httpURL]
	
	
This will download the entire repo to a folder in your current local
directory.
	
	
	
	4.2 Pulling and Merging Requests
	--------------------------------
	
You can pull updated files from the online repo with:


		git pull
		
		
Make sure you are in the correct directory to begin with, then the 
command will pull any file that is new or has been updated. 

However merge conflicts will come up if a file that has been edited on 
your local has been attempted to have been updated. Upon returning to 
your IDE, you may be met with a message that reads you must reload the 
file. This will include all local changes and add in any new changes 
that had no conflicts with merging. 


Another thing, you cannot do a pull if you have not committed your local
edited work. Command prompt will tell you this when attempting a pull
while you have uncommitted local changes. 

