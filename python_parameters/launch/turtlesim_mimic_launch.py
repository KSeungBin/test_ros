from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            executable='mimic', # turtlesim 패키지 안에 mimic node가 내장되어 있음
            name='mimic',  # 내가 지정한 node name
            remappings=[    # 발행된 '/turtlesim1/turtle1/pose' 를 '/turtlesim2/turtle1/cmd_vel'에 발행
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        )
    ])