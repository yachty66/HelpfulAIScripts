from setuptools import setup, find_packages

setup(
    name='helpful_ai_scripts',
    version='0.1.0',
    description='A collection of helpful AI scripts',
    author='Max Hager',
    author_email='maxhager28@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)