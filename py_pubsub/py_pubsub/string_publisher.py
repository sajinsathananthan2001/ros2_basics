#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
import rclpy.publisher


class StringPublisher(Node): 
    def __init__(self):
        super().__init__("string_publisher") 
        self.publisher = self.create_publisher(String,"my_message",qos_profile=10)
        self.timer = self.create_timer(1,self.stringCB)
        self.get_logger().info("The Node started!")

    def stringCB(self):
        msg = String()
        msg.data = "I'am a String publisher!"
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
