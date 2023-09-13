from setuptools import setup, find_packages

setup(
    name='portfolio-optimization',
    version='0.1.0',
    packages=find_packages(include=['portfolio_optimization.optimization.*'])
)
