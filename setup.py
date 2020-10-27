from setuptools import setup
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding = 'utf-8') as f:
    readme = f.read()

setup(
    name = 'countparticles',
    version = '1.1',

    description = 'Report the number of particles in each class from RELION',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Guillawme/countparticles',

    author = 'Guillaume Gaullier',
    author_email = 'contact@gaullier.org',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Natural Language :: English'
    ],
    keywords = 'cryo-EM particle class distribution visualization',

    py_modules = ["countparticles"],

    python_requires = '>=3.8.5',
    install_requires = [
        'click>=7.1.2',
        'matplotlib>=3.3.1',
        'starfile>=0.3.1'
    ],

    entry_points = {
        'console_scripts': [
            'countparticles=countparticles:cli'
        ]
    },

    project_urls = {
        'Bug Reports': 'https://github.com/Guillawme/countparticles/issues',
        'Source': 'https://github.com/Guillawme/countparticles'
    }
)
