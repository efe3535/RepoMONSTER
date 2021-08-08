from setuptools import setup

def install_needed():
    setup(
        name='RepoMONSTER',
        version='1.0',    
        install_requires=["colorama", "requests", "pyqt5", "gitpython", "tkinter"],
    )

install_needed()
