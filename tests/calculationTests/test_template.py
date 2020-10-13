
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentOfParentDir = os.path.dirname(parentdir)

#Allows imports from source folder.
sys.path.append(parentOfParentDir)

#!!!!!!!!!!!!!!!!!!!!!!!!name of file has to start with test_ !!!!!!!!!!!!!!!!!!!!!!!!!!

#import pytest necessary in testing file
import pytest

#!!!!!!!!!!!!!!!!! NAME OF MODULE/FILE YOU ARE TESTING FROM THE FOLDER YOU ARE TESTING FROM!!!!!!!!!!!!!!!!!!!!!!
#Ex if you are testing data_gen.py do import data_gen
from moreFunctions import template  


#Good practice to exapline in comments what is being tested

#!!!!!!!!!!!!!!!!!!!!! Test functions must use test_NAME convention or pytest will not run test !!!!!!!!!!!!!!!!!!!!

#---------------------------------------------
# Test subtract function that is in template that is supposed to 
# return a - b when given (a,b)
#---------------------------------------------

#Mark allows groups of tests to be run from command line
# @pytest.mark.NAMEOFMARK

@pytest.mark.calculations
def test_subtract():
	assert template.subtract(3,2) == 1

@pytest.fixture
def addToThree():
	x = 3
	return x


#---------------------------------------------
# addToThree is run as a fixture function 
# return value can be passed into test and used later
#---------------------------------------------

def test_variableInAddToThree(addToThree):
	assert (addToThree + 4) == 7


#====== RESOURCES =========
#
# General Pytest Tutorials: https://www.youtube.com/watch?v=byaxg00Gf9I
#
# Fixtures: Runs a function before all tests. Can make tests a faster if the output of function never changes. Used when output is fixed 
#              https://www.tutorialspoint.com/pytest/pytest_fixtures.htm#:~:text=Fixtures%20are%20functions%2C%20which%20will,some%20sort%20of%20input%20data.&text=A%20test%20function%20can%20use,name%20as%20an%20input%20parameter.
#
# Custom Marks: Used to group certain test together. These marked test can be run on the command line based on type of mark given.
#              https://docs.pytest.org/en/2.9.1/example/markers.html
#


