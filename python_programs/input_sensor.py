import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

TIMER_INTERVAL = 1.0

class Sensor(Node):
    def __init__(self):
        super().__init__('sensor')
        self.pub_sensor = self.create_publisher(Bool, 'input/sensor', 10)
        self.timer = self.create_timer(TIMER_INTERVAL, self.timer_callback)

    def timer_callback(self):
        sensor_msg = Bool(data=self.get_sensor_data())
        self.get_logger().info('publish sensor data: {}'.format(sensor_msg.data))
        self.pub_sensor.publish(sensor_msg)

    def get_sensor_data(self):
        return True


def main(args=None):
    rclpy.init(args=args)
    node = Sensor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()