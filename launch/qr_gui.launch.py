from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    qr_pose_pub = Node(
        package='goal_sender',
        executable='qr_pose_pub'
    )
    
    qr_reader = Node(
        package='goal_sender',
        executable='qr',
    )

    return LaunchDescription([
        qr_reader,
        qr_pose_pub,
    ])
