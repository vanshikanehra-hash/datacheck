from setuptools import setup, find_packages

setup(
    name="datacheck",
    version="0.1.0",
    author="Vanshika Nehra",
    description="A CLI tool to audit any dataset for quality issues.",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","numpy>=1.21.0"],
    entry_points={"console_scripts": ["datacheck=datacheck.cli:main"]},
    python_requires=">=3.8",
)