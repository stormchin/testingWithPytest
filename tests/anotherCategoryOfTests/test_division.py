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
from anotherCategoryOfFunctions.divisionFunctions import division

@pytest.mark.division
@pytest.mark.calculations
def test_divisionFunc():
    assert division.divisionFunc(6,3) == 2