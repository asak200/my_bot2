import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, RegisterEventHandler
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch.event_handlers import OnProcessStart

from launch_ros.actions import Node

def generate_launch_description():
    
    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    package_name='my_bot2'

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','rsp.launch.py'
        )]), launch_arguments={'use_sim_time': 'false', 'use_ros2_control': 'true'}.items()
    )

    ser_com = Node(
        package='serial_com',
        executable='serial_com',
    )

    joint_broad = Node(
        package='serial_com',
        executable='joint_broad',
    )
    
    diff_cont = Node(
        package='serial_com',
        executable='diff_cont',
        output='screen',
    )

    return LaunchDescription([
        rsp,
        ser_com,
        joint_broad,
        # diff_cont,
    ])
