from setuptools import setup

def get_long_description() -> str:
    with open("README.md") as file:
        return file.read()

setup(
    name="separse",
    description="A secure parser of math expressions from str.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version="1.0.0",
    author="DWolf_19",
    license="MIT License",
    url="https://github.com/DWolf-19/separse",
    packages=["separse"],
)
