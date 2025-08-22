"""
Setup.py file is essential for packaging and distribution of python projects.
it is used by setuptools library to define the configration of the projects, such as metadata, dependencies etc
"""

from setuptools import find_packages, setup
#find_packages will scan through the folders and check __init__.py files and mark that folder as main package and sub packages
from typing import List

def get_requirements()->List[str]: #type hints/type annotations as string
    """
    This function will retrun the list of required packages for the setup
    
    """
    requirement_lst:List[str]=[]

    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip() #The strip() function in Python is used to remove leading and trailing characters from a string
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt is not found")

    return requirement_lst


print(get_requirements())

setup(

    name="NetworkSecurity",
    version="0.0.1",
    author="Ishtiaq Ahmed",
    author_email="ishtiaqahmedz@yahoo.com",
    packages=find_packages(),
    install_requires=get_requirements()


)