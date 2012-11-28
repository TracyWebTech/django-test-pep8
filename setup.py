# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-test-pep8',
    version='0.1',
    description='PEP8 Tests to Django projects',
    long_description='PEP8 Tests to Django projects',
    keywords='django test pep8',
    author='Davi Oliveira',
    url='https://github.com/TracyWebTech/django-test-pep8',
    download_url='https://github.com/TracyWebTech/django-test-pep8/downloads',
    license='BSD',
    packages=find_packages(),
    install_requires=['pep8', ],
)
