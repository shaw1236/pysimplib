import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="simonpysimplib",
    version="0.0.1",
    description="Test the packing of a pypi module",
    long_description=README,
    url="https://github.com/shaw1236/pysimplib",
    author="Simon Li",
    author_email="shaw1236@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=[],
    include_package_data = True,
    install_requires=[]
)
