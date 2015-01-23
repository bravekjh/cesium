import numpy as np

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('common_functions', parent_package, top_path)

    config.add_extension('_lomb_scargle', '_lomb_scargle.pyx',
                         include_dirs=[np.get_include()])

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
