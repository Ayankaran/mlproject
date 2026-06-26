from setuptools import setup, find_packages
hyphen_e="-e ."
def get_requirements(filename):
    requirements = []
    with open(filename) as file_name:
        requirements = file_name.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        requirements = [req for req in requirements if req != hyphen_e]

setup(
    name='mlproject',
    version='0.0.1',
    
    author='Ayan Karan',
    author_email='ayankaran1271@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)