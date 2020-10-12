Testing resources for HUME-ICCAE 
================================
<img src="https://headlesstesting.com/assets/blog/2020/08/xpytest-ff7024fe91bfbe468ee6d515272ed904829eccdc02b7fd757e1ecc0bd5a9f4fc.png.pagespeed.ic.jaL31NSKZ6.webp" alt="mypy logo" width="300px"/>

# Contents
[Run Tests])(#Commands-To-Run-Tests)

[How to Create a Test](#How-To-Create-a-Test)

[Mark Tests (Markers)](#Mark-Tests)

[Create Fixtures](#Create-Fixtures)

[Resources](#Resources)

# How To Create a Test
[Create a Testing File](##Create-a-Testing-File)

[Create a Testing Function](##Create-a-Testing-Function)

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


# Mark Tests
# Create Fixtures
# Resources



