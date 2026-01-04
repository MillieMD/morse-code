from setuptools import setup

setup(
    name = 'morsecode',
    version = '0.1.0',
    packages = ['morsecode'],
    entry_points = {
        'console_scripts': [
            'morse-code = morsecode.__main__:main'
        ]
    })