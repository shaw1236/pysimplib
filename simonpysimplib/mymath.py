#$ python setup.py sdist bdist_wheel 
#$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
#$ pip install --index-url https://test.pypi.org/simple/ --no-deps simonpysimplib-shaw1236
#>>> import simonpysimplib

def myadd(a, b):
    return a + b

def mysub(a, b):
    return a - b

def mymul(a, b):
    return a * b

def mydiv(a, b):
    if b == 0:
        return 0
    else:
        return a / b

