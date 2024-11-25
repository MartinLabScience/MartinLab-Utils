from setuptools import setup, find_packages

setup(
    name="martinlab-utils",
    version="0.1.0",
    author="Martin Lab",
    description="Utilities used by Martin Lab members for teaching and research.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MartinLabScience/MartinLab-Utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
