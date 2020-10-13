import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentOfParentDir = os.path.dirname(parentdir)
sys.path.append(parentOfParentDir)

#Make this test pass
def test_syntax(self):
    if(x):
        assert True
