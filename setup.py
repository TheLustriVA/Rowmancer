from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='RowMancer',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'RowMancer=RowMancer.cli:cli',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
