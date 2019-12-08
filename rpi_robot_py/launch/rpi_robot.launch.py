

from  launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rpi_robot_py',
            node_executable='human_sensor',
        ),
        Node(
            package='rpi_robot_py',
            node_executable='servo',
            output='screen'
        ),
        Node(
            package='rpi_robot_py',
            node_executable='controller',
        )
    ])