# Django Test PEP8

Django APP to run PEP8 tests in your project.   
    
This app uses [pep8 package](http://pypi.python.org/pypi/pep8) to run tests.


## Installation

### Install package
To install using pip
```bash
pip install django-test-pep8
```
To install using easy_install
```bash
easy_install django-test-pep8
```

### Add test_pep8 to your settings.INSTALLED_APPS
```python
INSTALLED_APPS = (
    # your apps,
    test_pep8,
)
```

### Add your project base path to settings.TEST_PEP8_DIRS
```python
PROJECT_DIR = os.path.dirname(__file__)
TEST_PEP8_DIRS = [os.path.dirname(PROJECT_DIR), ]
```

### Other options
```python
TEST_PEP8_EXCLUDE = ['migrations', ] # Exclude this paths from tests
TEST_PEP8_IGNORE = ['E128', ] # Ignore this tests
```

## Running Tests
To run all tests
```bash
python manage.py test
```

To run pep8 tests only
```bash
python manage.py test test_pep8
```