from setuptools import setup, find_packages

setup(
    name='booklover',
    version='1.0.0',
    url='https://github.com/jjg5fg/booklover.git',
    author='Jack Gallagher',
    author_email='jjg5fg@virginia.edu',
    description='Tracker for books read',
    packages=find_packages(), 
    install_requires=['pandas >= 0.2'],
)
