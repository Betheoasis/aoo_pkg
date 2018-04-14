from distutils.core import setup

with open('README') as file:
    readme = file.read()

# NOTE: change the 'name' field below with some unique package name.
# then update the url field accordingly.

setup(
    name='aoo_pkg',
    version='2.0.0',
    packages=['wargame'],
    url='https://testpypi.python.org/pypi/aoo_pkg/',
    license='LICENSE.txt',
    description='test pkg ignore',
    long_description=readme,
    author='Betheo Asis',
    author_email='betheoasis@protonmail.com'
)
