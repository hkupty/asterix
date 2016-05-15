"""Asterix setup file"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='asterix',
    version='0.0.2',
    description=' Manage python components startup quickly and efficiently',
    long_description=long_description,
    url='https://github.com/hkupty/asterix',
    author='Henry "Ingvij" Kupty',
    author_email='hkupty@gmail.com',
    license='MIT',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='component management system startup',
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    py_modules=["asterix"],
    # install_requires=['peppercorn'],
    # extras_require={
        # 'dev': ['check-manifest'],
        # 'test': ['coverage'],
    # },
)
