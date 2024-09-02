from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():

    position_publisher = Node(
        package='goal_sender',
        executable='get_pose',
        output='screen',
    )
    
    raw_map_saver = Node(
        package='goal_sender',
        executable='image_saver_node',
    )

    map_updater = Node(
        package='goal_sender',
        executable='map_updater'
    )

    qr_pose_pub = Node(
        package='goal_sender',
        executable='qr_pose_pub'
    )

    delayed_qr_pose_pub = TimerAction(period=3.0, actions=[qr_pose_pub])

    return LaunchDescription([
        position_publisher,
        raw_map_saver,
        map_updater,
        delayed_qr_pose_pub,
    ])
