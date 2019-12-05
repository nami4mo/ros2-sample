# https://github.com/ros2/demos/blob/master/demo_nodes_py/setup.py

from setuptools import find_packages
from setuptools import setup

package_name = 'my_first_ros2'

setup(
    name=package_name,
    version='0.0.1',
    packages='',
    py_modules=[
        'python_programs.input_sensor',
        'python_programs.output_servo'
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
            'sensor = python_programs.input_sensor:main',
            'servo = python_programs.output_servo:main',
            # 'listener = demo_nodes_py.topics.listener:main',
            # 'talker = demo_nodes_py.topics.talker:main',
            # 'listener_qos = demo_nodes_py.topics.listener_qos:main',
            # 'talker_qos = demo_nodes_py.topics.talker_qos:main',
            # 'listener_serialized = demo_nodes_py.topics.listener_serialized:main',
            # 'add_two_ints_client = demo_nodes_py.services.add_two_ints_client:main',
            # 'add_two_ints_client_async = demo_nodes_py.services.add_two_ints_client_async:main',
            # 'add_two_ints_server = demo_nodes_py.services.add_two_ints_server:main'
        ],
    },
)