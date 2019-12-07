from setuptools import setup

package_name = 'rpi_robot_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ns',
    maintainer_email='ns@hoge.com',
    description='sample robot program',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'human_sensor = rpi_robot_py.input_human_sensor:main',
            'servo = rpi_robot_py.output_servo:main',
        ],
    },
)
