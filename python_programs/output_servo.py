import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class Servo(Node):
    def __init__(self):
        super().__init__('servo_node')
        self.sub_sensor = self.create_subscription(Bool, 'input/sensor', self.sensor_callback, 10)

    def sensor_callback(self, msg):
        self.get_logger().info('subscribr sensor data: {}'.format(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = Servo()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()