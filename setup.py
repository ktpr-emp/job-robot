from setuptools import setup, find_packages
import sys

sys.path.append('./job-robot/tests')

setup(
    name = 'Hoge',
    version = '0.1',
    description='This is test codes for travis ci',
    packages = find_packages(),
    test_suite = 'hoge_test.suite'
)
