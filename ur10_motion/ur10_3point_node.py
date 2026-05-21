#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import time

class UR10ThreePointMotion(Node):
    def __init__(self):
        super().__init__('ur10_3point_motion')

        self.trajectory_publisher = self.create_publisher(
            JointTrajectory,
            '/joint_trajectory_controller/joint_trajectory',
            10
        )

        self.joint_names = [
            'shoulder_pan_joint',
            'shoulder_lift_joint',
            'elbow_joint',
            'wrist_1_joint',
            'wrist_2_joint',
            'wrist_3_joint'
        ]

        self.positions = [
            [0.0, -1.57, 1.57, 0.0, 0.0, 0.0],
            [1.0, -1.0, 1.0, -0.5, 0.5, 0.0],
            [-1.0, -1.2, 0.8, 0.5, -0.5, 0.0]
        ]

        self.get_logger().info("UR10 3-Point Motion Node Started")
        self.get_logger().info("Waiting 5 seconds for controller to be ready...")
        time.sleep(5)

        self.execute_sequence()

    def execute_sequence(self):
        for i, position in enumerate(self.positions):
            self.get_logger().info(f"=== Moving to Position {i+1}/{len(self.positions)} ===")
            self.send_joint_trajectory(position)
            time.sleep(6)

        self.get_logger().info("ALL 3 POSITIONS COMPLETED!")

    def send_joint_trajectory(self, target_positions):
        msg = JointTrajectory()
        msg.joint_names = self.joint_names

        point = JointTrajectoryPoint()
        point.positions = target_positions
        point.time_from_start.sec = 4
        point.time_from_start.nanosec = 0

        msg.points = [point]

        self.trajectory_publisher.publish(msg)
        self.get_logger().info(f"Published: {target_positions}")

def main(args=None):
    rclpy.init(args=args)
    node = UR10ThreePointMotion()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
