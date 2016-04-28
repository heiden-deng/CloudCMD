from setuptools import setup
import sys
import os

packages = [
    'speedycmd',
]

if sys.version_info < (2, 6):
    error = 'ERROR: speedy-cmd requires Python Version 2.6 or above.'
    print >> sys.stderr, error
    sys.exit(1)

if not os.path.exists(os.path.expanduser('~') + "/.speedycfg"):
    cfg = open(os.path.expanduser('~') + "/.speedycfg", "w")
    cfg.write("ACCESS_KEY = your access_key\n")
    cfg.write("SECRET_KEY = your secret_key")
    cfg.close()

setup(
    name='speedycloudcmd',
    version='1.0',
    packages=packages,
    include_package_data=True,
    entry_points={
        'console_scripts': ['censor = speedycmd.speedycmd:execute']
    },
)
