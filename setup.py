import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'libcn',
    packages = setuptools.find_packages(),
    version = '0.0.2',
    description = 'Unofficial cyphernode library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'BHodl',
    author_email = 'hodlb@protonmail.com',
    url = 'https://github.com/BHodl/libcn',
    keywords = ['cyphernode', 'bitcoin', 'api', 'lightning'], 
    install_requires=[
        'argparse',
        'configparser',
        'requests',
        'urllib3',
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)