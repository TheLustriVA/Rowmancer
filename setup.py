from setuptools import setup, find_packages

setup(
    name='RowMancer',
    version='0.1.0',
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
)
