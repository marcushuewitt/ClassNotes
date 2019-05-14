
[TOC levels=1,2,3 numbered]: # "Class02"

# Class02
- [Class02](#class02)
- [Objectives:](#objectives)
- [Agenda](#agenda)
- [C2, Ex01 - Pull the latest class notes to your local copy of the class repo.](#c2-ex01---pull-the-latest-class-notes-to-your-local-copy-of-the-class-repo)
- [C2, Ex02](#c2-ex02)
- [C2, Ex03](#c2-ex03)
- [Installation of Python and VSCode](#installation-of-python-and-vscode)
  - [The two major version of Python](#the-two-major-version-of-python)
- [Introduction to VSCode](#introduction-to-vscode)
  - [Theming](#theming)
    - [Color Theme](#color-theme)
    - [Icon Theme](#icon-theme)
    - [The view menu](#the-view-menu)
    - [Setting keybindings](#setting-keybindings)
  - [General Settings](#general-settings)
  - [Adding extensions](#adding-extensions)
  - [Code Editing in VSCode](#code-editing-in-vscode)
    - [Multiple cursors](#multiple-cursors)
  - [Starting a bash terminal inside VSCode](#starting-a-bash-terminal-inside-vscode)
  - [VSCode and Git](#vscode-and-git)
- [Introduction to Markdown](#introduction-to-markdown)
- [C2, Ex04 (the assignment formally known as Assignment01, Part04)](#c2-ex04-the-assignment-formally-known-as-assignment01-part04)
- [Next steps](#next-steps)

# Objectives:
* Review last class, and get more practice with Git
* Install Python and VSCode
* Understand basic navigation and use of VSCode 
* Understand how to create documentation using Markdown
* Write your first program

# Agenda
* Review and discuss Assignment01 from last Class.
* Complete Assignment01 part 4 as an exercise
* Complete two additional exercises:
  * Create a local repo, then push it to GitHub
  * Pull request changes to a class repo
* Discuss programming/coding learning "journey" (and how frustration is most likely a necessary part of the process)
* Install Anaconda Python and VSCode
* Write and run your first program
* Setup VSCode as default editor for git

# C2, Ex01 - Pull the latest class notes to your local copy of the class repo.

If you look on the github class website, inside the ClassNotes repo you will see that I've added new content for class02. 

Use the github web interface to explore these changes (the professor will demonstrate)

* Now, let's commit these changes to your local copy of the ClassNotes repo. 

* Open a bash terminal and cd into your itm695/ClassNotes folder. 

* Now, pull the latest content found on github into your local copy of the repo (`git pull origin master`)

* Verify that you now have a Class02 folder and content within your local folder. 


# C2, Ex02

Let's add a few directories to your ST?? repo (your private repo). From last class, you should have your ST?? repo within your itm695 directory. 

* Open up a bash terminal and navigate to your ST?? repo.
* Create 6 folders:
  * Tests
  * Assignments
  * Exercises
  * Journal
  * Sandbox
  * Notes
* Using bash, within each folder, create a README.md file (note that case matters, so be sure to match the case of any commands and file names). Within each readme file should be one line, `#<First Name> <Last Name>, <Folder Name>`.
* Once you've made these changes, add these to staging, commit with a message "added default folder structure for private repo", and push the updates to the github server.
  

# C2, Ex03

So far, you've primarily been creating repos on GitHub, then cloning these to your local harddrive. Though this is probably the most common approach, there are times where you may want to create the local repo (by local, I mean on your machine) first, and then push the repo up to GitHub (or other repo servers).

Here are the steps:
* cd to your itm695 folder. 
* Create a directory called c02ex03
* cd into this directory
* initialize a new repo inside this directory (`git init`)
* Now, since this repo was not cloned from GitHub, github has not knowledge of this new repo. So, you will first create a new repo on github and set this as a remote repository. 
  * Log into github and create a repo in your public area (the professor will show this on the screen). Call this repo `C02EX03`. Copy the address of this repo to the clipboard. 
  * Once you've created your repo on github, go back to your bash terminal and add your new git repos as a remote. (`git remote add origin master <the address to the github repo>`)
  * Now, run the following command to verify that the remote called "origin" is setup (`git remote -v`) (NOTE: -v is a switch that tells git remote to display in verbose (aka, lot's of detail))
* using bash, create a README.md file containing one line "#C02Ex03"
* Commit this change. 
* Push this change to the remote respo (on github)
* Verify that this change had been uploaded into your github repo.
* From now on, when you want to push, or pull, content, `origin` is the remote github repo. NOTE: You can have multiple remotes, and give them unique names. By convention, origin is typically used as the name of a single remote repo server
 

# Installation of Python and VSCode

## The two major version of Python

There are two versions of Python, the 2.x series, and the 3.x series. Unlike most languages that retain backward compatibility, version 3.x python shed some of the old ways of working in python. This was necessary to clean up and refresh the language (other languages, such as Java, have retained backward compatibility, but it also creates a lot of complexity as new layers of ways of doing things are plastered on top of old ways. With Python's clean break from the past, there were free to make changes and not increase the complexity of working in the language by having to retain old ways of doing things. There was a downside to this approach though, and that is that early Python programs needed to be "ported" (a computer programming term for rewriting the program) for the new Python 3.x language. Also, programmers had to learn the new syntax and concepts, and many were reluctant. It has taken many years, but much of the Python codebase has been ported to version 3.x, and most programmers now use the new version.


Download and install the Anaconda Python distribution (https://anaconda.org/tcsmith314/dashboard)

NOTE: See [here](anaconda_install.md) for detailed steps.

Anaconda has the option to install VSCode. 

# Introduction to VSCode 

VSCode is an open-source project supported by Microsoft. When programming, programmers needs special tools to create, edit, run, and debug their code. The most basic of these tools is a Text Editor (for instance, MS Windows has a built in text editor, Notepad. Though you could use Notepad for your development, but there are better options.)

[Introduction](https://code.visualstudio.com/docs/introvideos/basics)

## Theming

### Color Theme

`<CMD-SHIFT-P>` then type "Preferences: Color theme" (without the quotes), and then select from a list of themes available

### Icon Theme

`<CMD-SHIFT-P>` then type "Preferences: Icon theme" (without the quotes), and then select from a list of themes available. I recommend keep the default "seti-theme" - the details of which can be found [here](https://marketplace.visualstudio.com/items?itemName=qinjia.seti-icons)

### The view menu

There are many option in the view menu that allow you to customize the layout of VSCode -- split views vertically, horizontally, move the side bar to the right, etc. 

### Setting keybindings

Unless you're an experienced programmer whose used another editor and would like to emulate that editors keybindings (which I don't believe anyone in class is), then I'd suggest just keeping the defaults. You can download a pdf of the defaults keybinding by typing `<CMD-SHIFT-P>` then type "keyboard`, then selecting "Help: Keyboard Shortcuts Reference".

## General Settings

VSCode is very configurable. VSCode stores all it's settings in a JSON file format (don't worry, it's pretty easy to read). To access this, type `<CMD-SHIFT-P>` then type "settings", then in this list select `Preferences: Open Settings JSON` (but there is also OPEN Settings UI). BE CAREFUL!!! It's probably best to leave these settings along until you have more experience with using VSCode. 

## Adding extensions

One powerful feature of VSCode is that there are many programmers that have developed extensions for VSCode. 

To view available extensions, and install/uninstall extensions, selecdt the extensions icon on the activity bar (it's the square looking icon the the far left of the VSCode interface)

The professor will demonstrate this, and suggest a few extensions to install. 

## Code Editing in VSCode

Global find a replace (it's the magnifying glass icon in the activity bar)

Linter/Linter - Linters help identify errors in your code. There are linters for various languages. There is a Python linter available. When the linter is installed, it will help identify issues in your code by providing an error indication (such as a red underline)

### Multiple cursors

Hold down the option key while you left click inside your open file in vscode. Each time you click, you get a new cursor added. Now when you type, what you type will go to each cursor location. To get back to a single cursor, press `ESC`.

Often you want to move a line of code. Simply move your cursor to the line you whish to move, and use `option` up or down arrow. 

There are many other code editing features available:

This is a particularly good reference: https://code.visualstudio.com/docs/editor/codebasics

This one is well (https://code.visualstudio.com/docs/editor/editingevolved), but it makes reference to code ideas (like symbols, etc.) that won't make sense until we begin developing python programs. 

## Starting a bash terminal inside VSCode

The key combination of tick and control will open up a terminal inside your VSCode window. You can also open a terminal by typing `<CMD-SHIFT-P>` and typing terminal, and then selecting 'Terminal: Create a New Integrated Terminal...".

Also, for windows, the default the shell used will be PowerShell (new versions of windows), or CMD (older versions). To set it to bash, you'll need to go to user settings, and change the shell used by windows in VSCode. The default path for a git bash terminal is "C:\\Program Files\\Git\\bin\\bash.exe". <CMD-SHIFT-P>, then select "Preferences: Open user settings". In the menu that pops up, SELECT "features", then "terminal", and then look for `External: Windows Exec Customizes which terminal to run on Windows.` Set this to bash. 
`

See here for more information on working with Terminal in VSCODE (https://code.visualstudio.com/docs/editor/integrated-terminal)


## VSCode and Git

VSCode support Git. In the activity bar there is a Git icon. When in a repo folder, git will display changes made to your code since the last commit. 

# Introduction to Markdown

See [here](markdown_intro.md)

# C2, Ex04 (the assignment formally known as Assignment01, Part04)

Using VScode, add an entry to your Journal folder found in your private repo (ST???). The file name should be C01_journal_.md. 

Copy the content your write for your Journal from last class into the C01_journal.md file. 

Commit this change (with an appropriate message) and push this to github. Use the integrated terminal in VSCode to do this. 


# Next steps

You will now complete Assignment02. Also, you should now know how to create a Journal entry. Make sure you create a Journal entry and push it to you repo before you leave. 