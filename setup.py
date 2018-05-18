# -*- coding: utf-8 -*-
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='katatennis',
        version='0.1',
        description='KataTennis from codingdojo',
        long_description=long_description,
        url='https://github.com/loicbaron/KataTennis',
        author=u'loicbaron',
        author_email='loic.baron@gmail.com',
        license='GPLv3',
        packages=['katatennis'],
        include_package_data=True,
        install_requires=[
            'flask',
        ],
        classifiers=[
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
        keywords='kata codingdojo',
)
