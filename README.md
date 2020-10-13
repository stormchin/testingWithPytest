Testing resources for HUME-ICCAE 
================================
<img src="https://headlesstesting.com/assets/blog/2020/08/xpytest-ff7024fe91bfbe468ee6d515272ed904829eccdc02b7fd757e1ecc0bd5a9f4fc.png.pagespeed.ic.jaL31NSKZ6.webp" alt="mypy logo" width="300px"/>

# Contents
[Commands To Run Tests](#Commands-To-Run-Tests)

[How to Create a Test](#How-To-Create-a-Test)

[Mark Tests (Markers)](#Mark-Tests)

[Create Fixtures](#Create-Fixtures)

[Repo Structure](#Repo-Structure)

[Pytest Demo](#Pytest-Demo)

[Resources](#Resources)


# Commands To Run Tests

### Run All Tests

```bash

pytest

```

### Run Tests in a Directory


```bash

pytest folder1/

```

### Run Specific Test File

```bash

pytest test_NAME.py

```

### Run Specific Test by Keyword

```bash
pytest -k "MyClass and not method"
```

### Run Specifc Test by Marker

```bash
pytest -m markerName
```

# How To Create a Test
[Create a Testing File](#Create-A-Testing-File)

[Create a Testing Function](#Create-a-Testing-Function)

## Create a Testing File

Testing files need to be in the test folder. In the test folder choose the sub folder that corresponds to your group or the type of test you want to create. For example, if your test has to do with data generation, put create your test file in the data_gen sup folder. Read below for the mandatory file naming convetions. 

### Syntax

When creating test file with pytest you must prefix the file with test_ . If this is not done, the tests within the file will not run!!!!!

### Import modules

To access the fucntions you want to test, you must either have initalized the file or folder as a module with an __init__.py file . If you have not done this or for some reason it isn't working properly, you can put the following code at the top of your code. 

``` python
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentOfParentDir = os.path.dirname(parentdir)

#Allows imports from source folder.
sys.path.append(parentOfParentDir)

```

## Create a Testing Function

### Syntax

Whithin your testing file, you must prefix each function with test_ .

Example:

``` python
def test_AddTwo():
  assert addition(2,2) == 4
```

### Commenting 

In an open source project, it is good practice to comment above your tests so others can understand later. This will allow a problem to be easily diagnosed if the test fails in the future. Below is an example of good commenting procedure.  

``` python
from parentDir import file
import pytest 

# =============================================================================
#  Checks addition( a: int a, b: int ) to see if it accurately adds two numbers greater than 0. 
#  
#==============================================================================
def test_AddTwo():
  assert file.addition(2,2) == 4
  
# ======================================================================================
#  Checks subtraction(a: int, b: int) to see if it accurately subtracts two numbers greater than 0. 
#  
#=======================================================================================
def test_SubTwo():
  assert file.subtraction(2,2) == 4
  
```

# Mark Tests
Putting markers on a functions allows all the makred tests to be grouped during runtime. Examples, commands, and more information found below. 

### Registering a Marker
You cannot just create a random marker an use it. You must register a marker with pytest by doing the follwing. In the pytest.ini file you should see the follwing:

``` yaml
[pytest]
testpaths = tests
markers =
    calculations: mark a test as a calculation.
    multiplication: mark a test a multiplication function.
    division: mark a test as a division function.
```

The calculations, multiplication, and division are all markers I have registered in this repo. To register a marker with pytest, open this file (pytest.ini) and add your own markers like so:

``` yaml
[pytest]
testpaths = tests
markers =
    calculations: mark a test as a calculation.
    multiplication: mark a test a multiplication function.
    division: mark a test as a division function.
    marker: mark a test with your own marker
```

If  you use a marker that is not registered, you may get an error or a warning. This may mess with your testing. It is highly reccomended to register markers in the configuration file. For the hume project, do not add any new markers without discussing it with your team. 

### Using a Marker

When trying to mark a function, you must write a decorator before the function decleration.

For example, if I would like to put a marker called multiplication on a test function I would put @pytest.mark.multiplication. You can also put multiple markers on one function as shown below. Make sure your markers are registered.

``` python

import pytest 
from calcFunctions import multiplication

# ======================================================================================
#  Checks multiplication(a: int, b: int) to see if it accurately multiplies two numbers greater than 0. 
#  
#=======================================================================================

@pytest.mark.multiplication
@pytest.mark.calculations
def test_multiplicationFunc():
    assert multiplication.multiplicationFunc(3,4) == 12
```
Run your marked test with this [command](#Run-Specifc-Test-by-Marker).

# Create Fixtures

Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some data to the tests such as database connections, URLs to test, and some sort of input data. Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.

Make function a fixture by typing following above a function-

``` python

@pytest.fixture

```

You can now use the function name and pass it returns to other functions that you are testing!

# Repo Structure

The repo strucutre is as follows:

```bash

├───.pytest_cache
│   └───v
│       └───cache
├───calcFunctions
│   ├───divisionFunctions
│   │   └───__pycache__
│   ├───multiplicationFunctions
│   │   └───__pycache__
│   └───__pycache__
├───moreFunctions
│   └───__pycache__
├───tests
│   ├───badTestsFIXME
│   │   └───__pycache__
│   └───calculationTests
│       └───__pycache__
└───__pycache__

```

The structure mimics the hume-iccae repo.



# Pytest Demo

Requirements: Must have python3 and pip installed. 

**Step 1)** 

Clone the repo with this [link]().


**Step 2)** 

Install the pytest module using

```bash
pip install pytest
```


**Step 3)** 

Open terminal and navigate to repo folder ~testingWithPytest/


**Step 4)** 

Type the following command

```bash
pytest
```

**Step 5)** 

Fix the failed tests! These tests include syntax errors and calculation errors. The comments should be good enough for you to fix what is wrong with the testing function as well as the function. 

**Step 6)** 

Check the pytest.ini file for all the registered markers. Run marked test using the following command.

```bash
pytest -m nameOfMarker
```
**Step 7)** 

Explore the repo! If you need to create a test, feel free to come back here and checkout the test_template.py file. 


# Resources

[General Pytest Tutorial](https://www.youtube.com/watch?v=byaxg00Gf9I)


[Fixtures](https://www.tutorialspoint.com/pytest/pytest_fixtures.htm#:~:text=Fixtures%20are%20functions%2C%20which%20will,some%20sort%20of%20input%20data.&text=A%20test%20function%20can%20use,name%20as%20an%20input%20parameter)


[Custom Marks](https://docs.pytest.org/en/2.9.1/example/markers.html)


