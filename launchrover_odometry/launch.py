from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([Node(package='rover_odometry',executable='velocity'),
                              Node(package='rover_odometry',executable='coordinate')])