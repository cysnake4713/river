import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="river-engine",
    version="0.0.1a",
    author="cysnake4713",
    author_email="cysnake4713@gmail.com",
    description="A framework to synchronize between different data source",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cysnake4713/river-engine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)