# pip install setuptools

from setuptools import setup, find_packages

requirements = ["toml", "PyYAML", "pandas", "sqlalchemy", "numpy"]

setup(
    name="helpers",
    version="1.4",
    install_requires=requirements,
    packages=find_packages(),
    author="fab",
)
