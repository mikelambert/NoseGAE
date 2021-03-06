from setuptools import setup

DESCRIPTION = "NoseGAE: nose plugin for Google App Engine testing"

VERSION = '0.5.3'


setup(
    name='NoseGAE',
    version=VERSION,
    author="Jason Pellerin",
    author_email="jpellerin@gmail.com",
    maintainer="Josh Johnston",
    maintainer_email="johnston.joshua+nosegae@gmail.com",
    description=DESCRIPTION,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Testing"
    ],
    url='https://github.com/Trii/NoseGAE',
    download_url='https://github.com/Trii/NoseGAE/tarball/' + VERSION,
    license='BSD License',
    entry_points={
        'nose.plugins.0.10': ['nosegae = nosegae:NoseGAE']
    },
    py_modules=['nosegae'],
    install_requires=['nose>=0.10.1'],
    zip_safe=False
)
