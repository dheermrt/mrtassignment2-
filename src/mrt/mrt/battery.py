import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
class BatteryPublisher(Node):
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_=self.create_publisher(Float32MultiArray,'battery',10)
         
        self.timer=self.create_timer(1,self.battery_callback)
        self.i=0
    def battery_callback(self):
        
        x=100.00 *float((random.random()))
        temp = float(random.randint(-20,80))
        
        y=Float32MultiArray()
        y.data=[x,temp]

        
        self.publisher_.publish(y)
        self.get_logger().info(f'Publshing :{y.data[0]}, {y.data[1]}')
        self.i=self.i+1
def main(args=None):
    rclpy.init(args=args)
    battery_publisher = BatteryPublisher()
    rclpy.spin(battery_publisher)
    rclpy.shutdown()
if __name__=='__main__':
    main()
    

