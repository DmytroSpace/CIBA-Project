from setuptools import setup, find_packages

setup(
    name='CIBAProject',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'ciba_project = __main__:main',
        ],
    },
)