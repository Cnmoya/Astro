from Cython.Build import cythonize
from distutils.core import setup
import numpy as np
import sys
file_=sys.argv[2]
setup(name=file_+"_module",ext_modules=cythonize(file_),include_dirs=[np.get_include()])
