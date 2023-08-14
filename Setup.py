from setuptools import find_packages ,setup

from typing import lists

REQUIREMENTS_FILE_NAME ="requirements.txt"

def get_requirements()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirements_list = requirement_file_headlines()
        requirements_list = [requirement_name_replace("\n", ) for requirement_name in requirement_list]
    
setup(

       name="sensor" ,
version="0.0.1",  
author="monika",
author_email="monikamishra0000787@gmail.com",
packages=find_packages(),
istall_requires=get_requirements()
)


