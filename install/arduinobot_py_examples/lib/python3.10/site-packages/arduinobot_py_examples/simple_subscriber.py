import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")
        self.sub = self.create_subscription(String,"chatter",self.callback,10)
        self.get_logger().info("Subscribing to chatter topic")

    def callback(self,msg):
        self.get_logger().info("I heard: %s"% msg.data)

def main():
    rclpy.init()
    node = SimpleSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()