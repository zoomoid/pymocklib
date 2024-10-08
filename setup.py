import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

# This call to setup() does all the work
setup(
    name="pymocklib",
    version="1.0.4",
    description="A PYthON 3.10 lib thaT will MAkE you APpEAR WEaK ANd BUTT-HUrT on THe inTeRNET",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zoomoid/pymocklib",
    author="Alexander Bartolomey",
    author_email="occloxium@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["pymocklib"],
    include_package_data=True,
    install_requires=[],
)
