from distutils.command.install import install
from setuptools.command import easy_install

def install_needed():
    easy_install.main( ["colorama", "requests", "pyqt5", "gitpython"] )

install_needed()