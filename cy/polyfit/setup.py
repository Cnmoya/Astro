from Cython.Build import cythonize
from distutils.core import setup
import numpy as np
setup(name="polyC",ext_modules=cythonize("polyC.pyx"),include_dirs=[np.get_include()])
