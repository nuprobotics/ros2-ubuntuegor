import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.client = self.create_client(Trigger, '/spgc/trigger')
        self.declare_parameter('service_name', '/trigger_service')
        self.declare_parameter('default_string', 'No service available')
        self.message = self.get_parameter('default_string').get_parameter_value().string_value
        service_name = self.get_parameter('service_name').get_parameter_value().string_value
        self.srv = self.create_service(Trigger, service_name, self.service_callback)
        self.get_message()

    def get_message(self):
        if not self.client.wait_for_service(timeout_sec=5.0):
            return

        self.future = self.client.call_async(Trigger.Request())
        rclpy.spin_until_future_complete(self, self.future)
        self.message = self.future.result().message

    def service_callback(self, request, response):
        response.success = True
        response.message = self.message
        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
