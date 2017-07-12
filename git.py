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

	1.1 Installing GIT on Raspberry Pi
	1.2 Creating a Global User Account
	
	

2. Creating a Repository
	
	2.1 Creating a local repository
	2.2 Adding your repository to GIT
3.
4.

1. Install



	1.1 Install GIT on Raspberry Pi
	
	
To install GIT on a Raspberry Pi:


	sudo apt install git



	1.2 Creating a Global User Account
	
	
	git config --global user.name "Your Name"
	git config --global user.email "your@email"


Will create a username and email for your account.

git config --global core.editor nano

This tells GIT which text editor you will use by default. In this 
instance we are using nano.


2. Creating a Repository
	2.1 Creating a local repository
	
	
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


	
	2.2 Adding your repository to GIT
	
To add your new file, use:

	
	git add README.md
	

You can also use the following to add every file in your current 
directory:


	git add --all
	
	
If you wish to see which files have been stage to commit, you can use:


	git status
	
	
To finally commit:


	git commit -am 'add README.md'
	
	
This commits everything that has been added or staged, and adds a 
comments 'add README.md' to the commit.
