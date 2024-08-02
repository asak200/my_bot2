import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    package_name = 'my_bot2'

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','my_onl_async.launch.py'
        )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','navigation_launch.py'
        )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    goal_sender = Node(
        package='goal_sender',
        executable='my_send_goal',
        output='screen',
    )

    return LaunchDescription([
        slam,
        nav2,
        # goal_sender,
    ])  
