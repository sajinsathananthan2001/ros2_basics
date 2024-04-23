## For create Cpp package in ROS2
To create a new package in ROS 2 for C++, you can use the `ros2 pkg create` command followed by the package name and optionally the dependencies. Here's how you can do it:

```bash
ros2 pkg create --build-type ament_cmake package_name
```

Replace `package_name` with the desired name of your package.

For example, if you want to create a package named "my_package" with C++ support, you would use the following command:

```bash
ros2 pkg create --build-type ament_cmake my_package
```
For adding dependencies within it:
```bash
ros2 pkg create --build-type ament_cmake --dependencies rclcpp package_name
```

## For create Python package in ROS2
To create a new ROS 2 package in Python with dependencies, you can use the `ros2 pkg create` command followed by the package name and the `--dependencies` flag specifying the dependencies. Here's how you can do it:

```bash
ros2 pkg create --build-type ament_python --dependencies package_dependency package_name
```

Replace `package_dependency` with the dependencies you want to include, separated by commas, and `package_name` with the desired name of your package.

For example, if you want to create a package named "my_python_package" with Python support and dependencies on `rclpy` and `std_msgs`, you would use the following command:

```bash
ros2 pkg create --build-type ament_python --dependencies rclpy,std_msgs my_python_package
```




## For remap the node with same name
In ROS 2, you can use the `__node:=new_node_name` argument to remap a node to a new name when launching it using the `ros2 run` command. Here's how you can do it:

```bash
ros2 run package_name executable_name --ros-args --remap __node:=new_node_name
```
Example:
```bash
ros2 run cpp_pubsub hello_world --ros-args --remap __node:=sajin
```
## For using --symlink-install(Only for python!)
Use this command to sync the package were you need not to give build multiple time for normal changes inn the node 

```bash
colcon build --packages-select cpp_pubsub --symlink-install
```

