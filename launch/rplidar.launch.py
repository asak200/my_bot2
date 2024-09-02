from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path = os.path.join(get_package_share_directory('my_bot2'))

    return LaunchDescription([
        Node(
            name='rplidar_composition',
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB2',
                'serial_baudrate': 115200,  # A1 / A2
                # 'serial_baudrate': 256000, # A3
                'frame_id': 'laser_frame',
                'inverted': False,
                'angle_compensate': True,
            }],
        ),

        # Node(
        #     package='laser_filters',
        #     executable='scan_to_scan_filter_chain',
        #     name='scan_filter',
        #     output='screen',
        #     parameters=[{'filter_chain': 'scan_filter_chain'},
        #                 os.path.join(pkg_path,'description','laser_limit.yaml')]
        # ),
    ])
