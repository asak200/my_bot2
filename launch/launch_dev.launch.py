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

    teleop_joy = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','joystick.launch.py'
        )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    twist_mux_params = os.path.join(get_package_share_directory(package_name), 'config', 'twist_mux.yaml')
    twist_mux = Node(
        package='twist_mux',
        executable='twist_mux',
        parameters=[twist_mux_params, {'use_sim_time': True}],
        remappings=[('/cmd_vel_out', '/diff_cont/cmd_vel_unstamped')]
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
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
        teleop_joy,
        twist_mux,
        rviz,
        # joint_broad,
        diff_cont,
    ])
