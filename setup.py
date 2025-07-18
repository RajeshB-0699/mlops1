from setuptools import setup, find_packages
from typing import List

hypen_e_dot = "-e ."

def get_requirements(filepath:str) -> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
    name='mlops1',
    version='0.0.1',
    author='Rajesh',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)