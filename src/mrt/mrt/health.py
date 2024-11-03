import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String 
 




class HealthPublisher(Node):
    def __init__(self):
        super().__init__('warning_publisher')
        self.subscription = self.create_subscription(Float32MultiArray,'battery',self.listener_callback,10)
        self.subscription
        self.publisher_ = self.create_publisher(String, 'warning',10)
         
         
    def listener_callback(self,y:Float32MultiArray):
        self.get_logger().info('I heard "%s"'%y.data[0])
        msg =String()    
        if(y.data[0]>=30):
            msg.data='Healthy'
        else:
            msg.data='Critical'

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing"%s"'%msg.data)
        

    
def main(args=None):
    rclpy.init(args=args)
    warning_publisher=HealthPublisher()
    rclpy.spin(warning_publisher)
    rclpy.shutdown()
if __name__ == '__main__':
    main()