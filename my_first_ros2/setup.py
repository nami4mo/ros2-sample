# https://github.com/ros2/demos/blob/master/demo_nodes_py/setup.py

from setuptools import find_packages
from setuptools import setup

package_name = 'my_first_ros2'

setup(
    name=package_name,
    version='0.0.1',
    packages='',
    py_modules=[
        'py_scripts.input_human_sensor',
        'py_scripts.sample',
        'py_scripts.output_servo'
    ],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='NS',
    author_email='ns@hoge.com',
    maintainer='NS',
    maintainer_email='ns@hoge.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='my first ros2 sample program',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'human_sensor = py_scripts.input_human_sensor:main',
            'sample = py_scripts.sample:main',
            'sample2 = py_scripts.sample2:main',
            'servo = py_scripts.output_servo:main',
        ],
    },
)