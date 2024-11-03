import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rover_simulation',
            executable='obstacle_avoidance_node',
             
            parameters=[{'grid': '0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0'}]),
        Node(
            package='rover_simulation',
            executable='rover_navigation_node',
             
            parameters=[{'start_position': '0,0', 'end_goal': '9,9'}]),
    ])