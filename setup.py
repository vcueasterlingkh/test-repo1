from setuptools import find_packages, setup


setup(
    name='testrepo1',
    version='0.1',
    description='Test repository',
    author='Chris Fauerbach',
    author_email='chfauerbach@vcu.edu',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)
