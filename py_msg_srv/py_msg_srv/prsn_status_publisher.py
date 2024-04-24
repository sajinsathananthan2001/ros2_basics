#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from custom_interfaces.msg import PersonStatus

class StatusPublisherNode(Node):
    def __init__(self):

        super().__init__('prsn_status_publisher')
        self.get_logger().info('Publisher started!')
        self.pub = self.create_publisher(PersonStatus,"/person_status",10)
        self.create_timer(0.5,self.send_prsn_status)

    def send_prsn_status(self):
        # self.get_logger().info("Hello World! "+str(self.counter))
        msg = PersonStatus()
        msg.name = "Sajin Sathananthan"
        msg.available = True
        msg.salary = 12000
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=StatusPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=='__main__':
    main()