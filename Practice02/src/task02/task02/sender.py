import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Sender(Node):
    def __init__(self):
        super().__init__('sender')
        self.declare_parameter('topic_name', '/spgc/receiver')
        self.declare_parameter('text', 'Hello, ROS2!')
        topic_name = self.get_parameter('topic_name').get_parameter_value().string_value
        self.publisher_ = self.create_publisher(String, topic_name, 10)
        self.broadcast()

    def broadcast(self):
        msg = String()
        msg.data = self.get_parameter('text').get_parameter_value().string_value
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    sender = Sender()

    rclpy.spin(sender)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
