cmake_minimum_required(VERSION 3.5)
project(cpp_pubsub)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

# we added------------------------------------------

add_executable(cpp_log_minimal src/log_minimal.cpp)
ament_target_dependencies(cpp_log_minimal rclcpp)

add_executable(cpp_log_minimal_oops src/log_minimal_oops.cpp)
ament_target_dependencies(cpp_log_minimal_oops rclcpp)

add_executable(hello_world src/hello_world.cpp)
ament_target_dependencies(hello_world rclcpp)

add_executable(string_publisher src/string_publisher.cpp)
ament_target_dependencies(string_publisher rclcpp example_interfaces)

add_executable(string_subscriber src/string_subscriber.cpp)
ament_target_dependencies(string_subscriber rclcpp example_interfaces)

install(TARGETS
  cpp_log_minimal
  cpp_log_minimal_oops
  hello_world
  string_publisher
  string_subscriber
  DESTINATION lib/${PROJECT_NAME}
)

# we added------------------------------------------

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
