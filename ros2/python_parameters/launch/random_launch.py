from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='simple_action_python',
            namespace='randomspace',
            executable='random_action_server',
            name='server'
        ),
        Node(
            package='simple_action_python',
            namespace='randomspace',
            executable='random_action_client',
            name='client'
        ),
    ])