#!/usr/bin/env python3
import os
from setuptools import setup


def read(fname,
         ):
    """Utility function to read the README file.
    Notes
    -----
    This is used for the long_description.
    """
    return open(os.path.join(os.path.dirname(__file__),
                             fname),
                'r').read()


setup(name="django-socialmeta",
      version="0.1",
      author="Gabriel Paul 'Cley Faye' Risterucci",
      author_email="gabriel.risterucci@gmail.com",
      description=("Helper tools to provide basic metatags in Django HTML "
                   + "output"),
      license="MIT",
      keywords="django meta social",
      url="https://repos.cleyfaye.net/trac/django-socialmeta",
      packages=['socialmeta',
                'socialmeta.mixins'],
      include_package_data=True,
      install_requires=['pycaptcha',
                        'django'],
      long_description=read('README.md'),
      python_requires='>=3',
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: "
          + "CGI Tools/Libraries",
          "Framework :: Django :: 1.11",
          "License :: OSI Approved :: MIT License",
      ],
      )
