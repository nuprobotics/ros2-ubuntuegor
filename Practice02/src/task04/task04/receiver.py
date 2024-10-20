import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
from sensor_msgs.msg import CompressedImage


class Receiver(Node):

    def __init__(self):
        super().__init__('receiver')
        self.stopped = False
        self.declare_parameter('topic_name', '/send_image_here')
        self.subscription = self.create_subscription(
            CompressedImage,
            self.get_parameter('topic_name').get_parameter_value().string_value,
            self.listener_callback,
            10)
        self.srv = self.create_service(Trigger, '/ubuntuegor/stop', self.service_callback)

    def service_callback(self, request, response):
        self.stopped = True
        response.success = True
        response.message = "ok"
        return response
    
    def listener_callback(self, msg):
        if self.stopped:
            return

        format = msg.format
        data = msg.data
        with open(f"last_image.{format}", "wb") as f:
            f.write(data)


def main(args=None):
    rclpy.init(args=args)

    receiver = Receiver()

    rclpy.spin(receiver)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
