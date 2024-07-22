import launch
import launch_ros.actions
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

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

    # Define the path to the launch XML file
    launch_file_path = 'launch.xml'

    # Include the launch XML file
    include_launch_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([launch_file_path]),
        launch_arguments={'some_argument': 'some_value'}.items()
    )

    # Create launch description
    ld = launch.LaunchDescription()

    # Add nodes and included launch description to launch description
    ld.add_action(node1)
    ld.add_action(include_launch_description)

    return ld
