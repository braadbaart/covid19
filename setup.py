import setuptools

with open("README.md", "r") as rdm:
    long_description = rdm.read()

setuptools.setup(
    name"covid19",
    version="0.0.1",
    description="COVID-19 intervention and spread models",
    long_description=long_description,
    packages=setuptools.find_packages(),
    python_requires=">=3.6"
)