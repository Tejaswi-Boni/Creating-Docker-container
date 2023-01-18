from setuptools import setup
from typing import List

#declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR ="Tejaswi"
DESCRIPTION ="this is housing prediction project"
PACKAGES = ["Housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    
    """
    Description : this function is going to return a list of requirements 
    mentioned in requirements.txt

    return : this function is going to return a list which contains the 
    name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = PACKAGES,
    install_requires = get_requirements_list()

)
