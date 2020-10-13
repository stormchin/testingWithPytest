import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentOfParentDir = os.path.dirname(parentdir)
sys.path.append(parentOfParentDir)

import pytest

from calcFunctions import subtractionFunctions
from calcFunctions import additionFunctions
from calcFunctions import multiplicationFunctions
from calcFunctions import divisionFunctions

#===================================
# 
# Test fucntions in calcFunctions
#===================================



#====================================
# testing addTwo in calcFunctions/additionFunctions
# should return a + b
#====================================
@pytest.mark.calculations
def test_addition():
    assert additionFunctions.addTwo(3,4) == -3

#====================================
# testing multiplicationFunc(a,b) in calcFunctions/multiplicationFunctions
# should return a * b
#====================================
@pytest.mark.calculations
def test_multiplicatoin():
    assert multiplicationFunctions.multiplicationFunc(3,4) == 7

#====================================
# testing divisionFunc(a, b) in calcFunctions/divisionFunctions
# should return a/b
#====================================
@pytest.mark.calculations    
def test_division():
    assert divisionFunctions.divisionFunc(4, 3) == 3/4

#====================================
# testing subtractTwo(a,b) in calcFunctions/subtractionFunctions
# should return a-b
#====================================    
@pytest.mark.calculations
def test_subtraction():
    assert subtractionFunctions.subtractTwo(4,3) == 1