"""A setuptools based setup module for A3 project.
   Based on <http://setuptools.readthedocs.io/en/latest/setuptools.html>
"""

from setuptools import setup, find_packages
setup(
    name="GroupF",
    version="1",
    packages=['project_app'],

    install_requires=['Flask==0.10.1','PyMySQL==0.6.7','Flask-SQLAlchemy==2.1','Flask-Script==2.0.5','Flask-WTF==0.12','Flask-Migrate==1.6.0','py-bcrypt==0.4','python-slugify==1.1.4','Flask-Markdown==0.3','Flask-Uploads==0.2.0'], # PyPI package

    package_data={

        '': ['*.txt', '*.pdf','*.db','*.pod'],

        'project_app': ['migrations/*','templates/*', 'main/*', 'templates/*','templates/includes/*','migrations/versions/*','doc/*'],
    },

    author="GroupF",
    author_email="zimam@mun.ca",
    description="This is project",
    license="COMP2005 students", 
    keywords="Our Project",
    url="http://www.cs.mun.ca/~brown/2005",   

)


