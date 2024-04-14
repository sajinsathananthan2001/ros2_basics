#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class HelloWorld(Node):
    def __init__(self):
        self.counter=0

        super().__init__('hello_world_node')
        self.get_logger().info('Hello World of ROS2!')
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello World! "+str(self.counter))
        self.counter+=1
    

def main(args=None):
    rclpy.init(args=args)
    node=HelloWorld()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=='__main__':
    main()