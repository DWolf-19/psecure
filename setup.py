import setuptools

def get_long_description() -> str:
    with open("README.md") as file:
        return file.read()

def parse_requirements() -> list[str]:
    with open("requirements.txt") as file:
        dependencies = (d.strip() for d in file.read().split("\n") if d.strip())
        return [d for d in dependencies if not d.startswith("#")]

setuptools.setup(
    name="psecure",
    description="A secure parser of math expressions from str.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version="1.0.0",
    author="DWolf_19",
    license="MIT License",
    url="https://github.com/DWolf-19/psecure",
    install_requires=parse_requirements(),
    packages=["psecure"],
)
