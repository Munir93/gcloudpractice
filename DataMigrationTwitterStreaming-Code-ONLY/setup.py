import setuptools
REQUIRED_PACKAGES = []
PACKAGE_NAME = 'textblob'
PACKAGE_VERSION = '0.15.1'
setuptools.setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='dataflow worker',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
)