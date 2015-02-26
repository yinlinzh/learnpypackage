# import os

# __version_os.path.dirname(__file__)

from setuptools import setup
# , find_packages

# with open() as f:

setup(
    name='learnpypackage',
    # version=version,
    version='1.0.0.dev',
    description='A toy project to learn Python packaging and distribution',
    url='',
    author='Yinlin Zhang',
    author_email='crackerzhang@gmail.com',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],
    keywords='sample distribution development',
    # packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    packages=['learnpypackage', 'learnpypackage.abc'],
    entry_points={
        'console_scripts': ['yinlinzhtest=learnpypackage.efg:main', ],
    }
)
