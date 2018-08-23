from setuptools import setup, find_packages

import krakenforwarder

setup(
    name='krakenforwarder2',
    version=krakenforwarder.__version__,
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    url='https://github.com/supercuiller/kraken_listener',
    license='MIT',
    author='Thibaut Castaings',
    author_email='castaings.t@protonmail.com',
    description='Forwards trades from Kraken.com to TCP port',
    long_description=open('README.md').read()
)