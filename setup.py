from setuptools import setup, find_packages

setup(
    name="splitwords",
    version="0.0.3",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "splitwords.dicts": ["dicts/*.txt"],
    },
    install_requires=[
        "numpy",
    ],
)