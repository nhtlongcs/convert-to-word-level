from setuptools import setup, find_packages

setup(
    name="split-vnm-words",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "splitwords.dicts": ["dicts/*.txt"],
    },
    install_requires=[
        "numpy",
    ],
)