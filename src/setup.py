from distutils.core import setup, Extension
import warnings
import setuptools

setup(name="rpidriver",
      version="1.0",
      description="sMap driver for reading ambient sensors from RPi",
      author="Pandarasamy Arjunan",
      author_email="pandarasamya@iiitd.ac.in",
      url="https://github.com/pandarasamy/AmbientMonitorRPiDriver/",
      license="",
      packages=[
        "rpidriver", 
        ],
      requires=["smap", ],
      classifiers=[
        'Development Status :: 1 - Beta',
        'License :: ',
        'Programming Language :: Python',
        ]
      )
