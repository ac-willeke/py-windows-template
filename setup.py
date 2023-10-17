from setuptools import find_packages, setup

requirements = [
    # package requirements go here
]

setup(
    name="windows-template",
    version="0.1.0",
    description="This repo is a python template for windows.",
    license="MIT",
    author="willeke acampo",
    author_email="willeke.acampo@nina.no",
    url="https://github.com/ac-willeke/urban-treeDetection",
    packages=find_packages(),
    install_requires=requirements,
)
