from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os
import xacro

def generate_launch_description():

    pkg_path = get_package_share_directory(
        'simple_mobile_robot'
    )

    xacro_file = os.path.join(
        pkg_path,
        'urdf',
        'simple_robot.urdf.xacro'
    )

    world_file = os.path.join(
        pkg_path,
        'worlds',
        'empty.world'
    )

    robot_description = xacro.process_file(
        xacro_file
    ).toxml()

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {'robot_description': robot_description}
        ]
    )

    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', world_file],
        output='screen'
    )

    spawn_robot = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='ros_gz_sim',
                executable='create',
                arguments=[
                    '-name', 'simple_mobile_robot',
                    '-topic', 'robot_description'
                ],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        robot_state_publisher,
        gazebo,
        spawn_robot
    ])