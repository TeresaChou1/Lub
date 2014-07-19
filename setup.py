from setuptools import setup
import os

required_modules = ['selenium','Appium-Python-Client','sure','fuzzywuzzy','python-subunit’,’lettuce’]

def get_packages():
    # setuptools can't do the job :(
    packages = []
    for root, dirnames, filenames in os.walk('Lub'):
        if '__init__.py' in filenames:
            packages.append(".".join(os.path.split(root)).strip("."))
    return packages

setup(
    name='Lub',
    version='0.1.1',
    description='Lub is a BDD automation testing Tool based on lettuce',
    author='Archer',
    author_email='qddegtya@gmail.com',
    url='http://www.diggerplus.org',
    packages=get_packages(),
    install_requires=required_modules,
    entry_points={
        'console_scripts': ['lub = Lub.bin:main'],
        },
    package_data={
        'lub': ['COPYING', '*.md'],
    },
)
