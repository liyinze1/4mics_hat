from setuptools import setup, find_packages

setup(
    name='respeaker',
    packages=find_packages(['interfaces', 'interfaces.*'])
)