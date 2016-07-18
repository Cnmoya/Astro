from Cython.Build import cythonize
from distutils.core import setup
import numpy as np
file_="overscan.pyx"
setup(name=file_+"_module",ext_modules=cythonize(file_),include_dirs=[np.get_include()])
