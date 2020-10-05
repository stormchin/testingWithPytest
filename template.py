#================================
# Function takes two integer values subtracts them and returns intger answer.
# Input: int a , int b
# Output:  a - b
#================================

#importing pytest so fixtures can be used

import pytest 

def subtract(a , b):
	return a - b

@pytest.fixture
def addToThree():
	x = 3
	return x