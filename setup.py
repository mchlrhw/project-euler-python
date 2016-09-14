#import ez_setup
#ez_setup.use_setuptools()

from setuptools import find_packages
from setuptools import setup


setup(
    name='euler',
    version='0.0.1',
    author='mrmrwat',
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
