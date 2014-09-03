python-ibconn
=============

python infoblox library

to build for local installation, do the following:

python setup.py sdist

this will generate a tar/zip file in the dist directory tagged with the version number defined in the setup.py file.
to install that file, use pip, forcing a reinstall if the version number has not incremented:

pip install dist/ibconn-0.1.0.tar.gz --force-reinstall -I

now the module should be importable in python via:

from ibconn import ibconn
