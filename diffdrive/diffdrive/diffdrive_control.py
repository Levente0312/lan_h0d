#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame
import sys

class DiffDriveController(Node):
    def __init__(self):
        super().__init__('diffdrive_controller')

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.linear_vel = 0.0
        self.angular_vel = 0.0
        self.timer = self.create_timer(0.1, self.update)

        pygame.init()
        pygame.display.set_mode((200, 200))
        pygame.display.set_caption("Diffdrive Control")

        self.get_logger().info("WASD vagy nyilak - irányítás és /cmd_vel topic üzenet")


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rclpy.shutdown()
                return
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    self.linear_vel = 1.0
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.linear_vel = -1.0
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.angular_vel = 1.0
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.angular_vel = -1.0
            elif event.type == pygame.KEYUP:
                # ha felengeded a gombot: megáll
                self.linear_vel = 0.0
                self.angular_vel = 0.0

        msg = Twist()
        msg.linear.x = self.linear_vel
        msg.angular.z = self.angular_vel
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DiffDriveController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
