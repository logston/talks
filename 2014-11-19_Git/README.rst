Intro to Git
============

by Paul Logston

This tutorial is based on a video tutorial by Scott Chacon. 

- Specifically the video at https://www.youtube.com/watch?v=OFkgSjRnay4
- His books is at: http://git-scm.com/book
- And he manages http://git-scm.com/
- Other resources: https://www.atlassian.com/git/

What is Git?
------------

Version Control System

Other common version control systems: Subversion, Mercurial

How does Git control versions?
It packages changes in sets of files into **commits**. 
Committing your work is the equivalent of taking a snapshot of what your files 
contain at a specific point in time. 

Graph Showing Status -> Change -> Status -> Change -> Status -> ...

A **repository** is a special type of directory in which all files within that 
directory are tracked by a collection of commits.

For this tutorial, we have a directory with two files that we want to track the
changes of with Git.

SimpleApp (direcotry)
    README.rst
    LICENSE
    index.html

First things first, let's do some one time tasks.



