from setuptools import setup, find_packages

requirements = ["toml", "PyYAML"]

setup(
    name="helpers",
    version="1.2",
    install_requires=requirements,
    packages=find_packages(),
    author="fab",
)
