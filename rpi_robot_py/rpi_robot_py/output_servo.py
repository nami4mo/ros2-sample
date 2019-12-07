import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
from rclpy.executors import MultiThreadedExecutor
from std_msgs.msg import Bool

import time
import Adafruit_PCA9685
import random

ANGLE_MIN = -70
ANGLE_MAX = 70


class Servo(Node):
    def __init__(self, servo_id, move_timing):
        super().__init__('servo_node_' + str(servo_id))
        self.servo_id = servo_id
        self.move_timing = move_timing
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(60)
        self.sub_sensor = self.create_subscription(Bool, '/input/human_sensor', self.sensor_callback, 10)


    def sensor_callback(self, msg):
        if self.move_timing == msg.data:
            self.get_logger().info('subscribr sensor data: {}'.format(msg.data))
            angle = random.randint(ANGLE_MIN, ANGLE_MAX)
            self.set_angle(angle)


    def set_angle(self, angle):
        angle = max(ANGLE_MIN, angle)
        angle = min(ANGLE_MAX, angle)
        pulse = (600-150) / 180 * (angle + 90) + 150
        self.pwm.set_pwm(self.servo_id, 0, int(pulse))


def main(args=None):
    rclpy.init(args=args)
    executor = MultiThreadedExecutor(num_threads=2)
    node_0 = Servo(servo_id=0, move_timing=True)
    node_3 = Servo(servo_id=3, move_timing=False)
    executor.add_node(node_0)
    executor.add_node(node_3)
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    executor.shutdown()
    node_0.destroy_node()
    node_3.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()