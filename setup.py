from setuptools import setup, find_packages

def dependencies(imported_file):
    """ __Doc__ Handles dependencies """
    with open(imported_file) as file:
        return file.read().splitlines()

setup(
    name="builtwithsubs",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'builtwithsubs=builtwithsubs.builtwithsubs:main',  # Adjust the import path for main
        ],
    },
    # install_requires=[],  # Add any dependencies if needed
    install_requires=dependencies('requirements.txt')
)
