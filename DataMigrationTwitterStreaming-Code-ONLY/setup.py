'''import setuptools
REQUIRED_PACKAGES = []
PACKAGE_NAME = 'textblob'
PACKAGE_VERSION = '0.15.1'
setuptools.setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='dataflow worker',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
)'''
import sys
import os
import subprocess
import pickle

import setuptools
import distutils

from setuptools.command.install import install as _install



class install(_install):  # pylint: disable=invalid-name
    def run(self):
        self.run_command('CustomCommands')
        _install.run(self)

CUSTOM_COMMANDS = [
    ['pip', 'install', 'textblob'],
]


class CustomCommands(setuptools.Command):
    """A setuptools Command class able to run arbitrary commands."""

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def RunCustomCommand(self, command_list):

        p = subprocess.Popen(
            command_list,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # Can use communicate(input='y\n'.encode()) if the command run requires
        # some confirmation.
        stdout_data, _ = p.communicate()

        if p.returncode != 0:
            raise RuntimeError(
                'Command %s failed: exit code: %s' % (command_list, p.returncode))

    def run(self):
        for command in CUSTOM_COMMANDS:
            self.RunCustomCommand(command)


REQUIRED_PACKAGES = [

]


setuptools.setup(
    name='name',
    version='1.0.0',
    description='DataFlow worker',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
    cmdclass={
        'install': install,
        'CustomCommands': CustomCommands,
        }
    )