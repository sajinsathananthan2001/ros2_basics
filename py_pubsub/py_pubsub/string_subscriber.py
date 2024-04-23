#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
import rclpy.publisher


class StringSubscriber(Node): 
    def __init__(self):
        super().__init__("string_subscriber") 
        self.subscriber = self.create_subscription(String,"my_message",self.stringDataCB,10)
        self.get_logger().info("The Node started!")

    def stringDataCB(self,msg):
        string_data = msg.data
        self.get_logger().info(string_data)


def main(args=None):
    rclpy.init(args=args)
    node = StringSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
