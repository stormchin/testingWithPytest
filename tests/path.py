#RUN THIS TO SEE THE DIRECTORY LOOKED AT TO IMPORT MODULES IN TESTING

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentOfParentDir = os.path.dirname(parentdir)
print("Current Path", currentdir)
print("Parent Directory", parentdir)
print("Parent of Parent Directory", parentOfParentDir)