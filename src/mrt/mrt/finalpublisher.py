import rclpy 
from rclpy.node import Node 
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String 
class FinalPublish(Node):
    def __init__(self):
        super().__init__('final_publish')
        self.subscription1=self.create_subscription(Float32MultiArray,'battery',self.listener_callback,10)
        self.subscription2=self.create_subscription(String,'warning',self.lisener_callback1,10)
        self.subscription1
        self.subscription2
    def listener_callback(self,y):
        self.get_logger().info('Battery"%s"'%y.data[0])
        self.get_logger().info('Temperature"%s"'%y.data[1])
    def lisener_callback1(self,msg):
        self.get_logger().info('Warning"%s"'%msg.data)
def main(args=None):
    rclpy.init(args=args)
    final_publish=FinalPublish()
    rclpy.spin(final_publish)
    rclpy.shutdown()
if __name__=='__main__':
    main()


        