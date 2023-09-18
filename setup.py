from setuptools import setup, find_packages

setup(
    name='cdr',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'rich',
        'toml',
        'csv'
    ],
    entry_points={
        'console_scripts': [
            'cdr=cdr.cli:cli',
        ],
    },
)
