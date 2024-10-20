import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage

class Sender(Node):

    def __init__(self):
        super().__init__('sender')
        self.stopped = False
        self.declare_parameter('topic_name', '/send_image_here')
        self.publisher_ = self.create_publisher(CompressedImage, self.get_parameter('topic_name').get_parameter_value().string_value, 10)
        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        msg = CompressedImage()
        msg.format = 'jpeg'
        with open('mario.jpg', "rb") as f:
            msg.data = f.read()
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    sender = Sender()

    rclpy.spin(sender)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
