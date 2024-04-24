#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from custom_interfaces.srv import RectangleArea


class RectangleAreaNode(Node):
    def __init__(self):
        super().__init__("rectangle_area")
        self.server = self.create_service(
            RectangleArea, "calculate_area", self.callback_add_two_ints)
        self.get_logger().info("Calculating area started.")

    def callback_add_two_ints(self, request, response):
        response.area = request.length * request.width
        self.get_logger().info(str(request.length) + " * " +
                               str(request.width) + " = " + str(response.area))
        return response


def main(args=None):
    rclpy.init(args=args)
    node = RectangleAreaNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
