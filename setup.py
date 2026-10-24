from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list:
    """this function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_object:
        requirements = [req.strip() for req in file_object.readlines()]
        requirements = [req for req in requirements if req]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

      
      
setup(
    name="ML_project",
    version="0.1",
    author="Hamza shahid",
    author_email="hamzashahid8587@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))