from Cython.Build import cythonize
from distutils.core import setup
import numpy as np
import sys
file_= "__struct__.pyx"
setup(name=file_+"_module",ext_modules=cythonize(file_),include_dirs=[np.get_include()])
