#!!!!!!!!!!!!!!!!!!!!!!!!name of file has to start with test_ !!!!!!!!!!!!!!!!!!!!!!!!!!

#import pytest necessary in testing file
import pytest

#!!!!!!!!!!!!!!!!! NAME OF MODULE/FILE YOU ARE TESTING !!!!!!!!!!!!!!!!!!!!!!
#Ex if you are testing data_gen.py do import data_gen
import template  


#Need comments explaing what is being tested
#Mark allows groups of tests to be run from command line
# @pytest.mark.NAMEOFMARK

#!!!!!!!!!!!!!!!!!!!!! Test functions must use test_NAME convention or pytest will not run test !!!!!!!!!!!!!!!!!!!!

#---------------------------------------------
# Test subtract function that is in template that is supposed to 
# return a - b when given (a,b)
#---------------------------------------------
@pytest.mark.calculations
def test_subtract():
	assert template.subtract(3,2) == 1


#---------------------------------------------
# Test addToThree function in template that is supposed to 
# return a + 3 when given (a)
#---------------------------------------------
def test_addThree():
	assert template.addToThree(7) == 10

def test_variableInAddToThree(template.addToThree):
	assert template.addToThree  == 3


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


# ---- Commands for running Tests -------
#
# With Marks:
# All tests: 
# Test in Folder: 
# Tests in file:
# One function with a specific name:
# Functions with similar names: 
