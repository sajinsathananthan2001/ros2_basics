import launch
import launch_ros.actions

def generate_launch_description():
    # Define nodes
    node1 = launch_ros.actions.Node(
        package='your_package_name',
        executable='your_node_executable',
        name='your_node_name',
        parameters=[
            {'param_name': 'param_value'}
        ]
    )

    # Create launch description
    ld = launch.LaunchDescription()

    # Add nodes to launch description
    ld.add_action(node1)

    return ld
