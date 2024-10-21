from setuptools import find_packages,setup
from typing import List


hyphen_e_dot ='-e .'

def get_requirements(file_path: str) -> List[str]:
        """this function will return a list of requirements"""

        requirements=[]
        with open(file_path, 'r') as file_object:
                requirements=file_object.readlines()
                requirements=[req.replace('\n','') for req in requirements]
                if hyphen_e_dot in requirements:
                    requirements.remove(hyphen_e_dot)    
        return requirements        





setup(
    name='my_package',
    version='0.1.0',
    description='A simple Python package',
    author='Saurabh yadav',
    author_email='sy669505@gmail.com',
    url='https://github.com/SaurabhYadav/my_package',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)