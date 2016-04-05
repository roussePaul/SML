## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
#TODO remove packages that are not used anymore
setup_args = generate_distutils_setup(
    packages=[
        'utilities',
        'simulators_hierarchical',
        'yaw_controllers',
        'systems_functions',
        'quadrotor_tracking_controllers_hierarchical',
        'controllers_hierarchical'
        ],
    package_dir={'': 'scripts'},
)

setup(**setup_args)
