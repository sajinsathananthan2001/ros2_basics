#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from custom_interfaces.action import CountUntil

import time

class CountUntilServerNode(Node): 
    def __init___(self):
        super().__init__("count_until_server")

        # action server
        self.count_until_server_ = ActionServer(
            self,
            CountUntil,
            "count_until",
            execute_callback=self.execute_callback())
        self.get_logger().info("Action server started!")
        
    def execute_callback(self,goal_handle : ServerGoalHandle):  #serverGoal type
        
        # Get requst from goal
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period

        # Execute the action 
        self.get_logger().info("Executing goal!")

        counter = 0 
        for i in range(target_number):
            counter+=1
            self.get_logger().info(str(counter))
            time.sleep(period)

        # Once done, set goal final state 
        goal_handle.succeed()

        # Send thee result 
        result = CountUntil.Result()
        result.reacheda_number = counter
        return result




def main(args=None):
    rclpy.init(args=args)
    node = CountUntilServerNode()   
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()