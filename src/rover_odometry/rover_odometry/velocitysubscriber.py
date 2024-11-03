import rclpy 
from rclpy.node import Node
from mars.msg import RoverOdometry
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String
import math

currentx=0.0
currenty=0.0
currentz=0.0
class coordinateupdater(Node):
    def __init__(self):
        super().__init__('position_updater')
        self.subscription = self.create_subscription(RoverOdometry,'motiondata',self.update,10)
        self.publisher1 = self.create_publisher(Float32MultiArray,'positioncoordinates',10)
        self.publisher2 = self.create_publisher(String,'warning',10)
    def update(self,msg):
        
        global currentx,currenty,currentz
        currentx=currentx+msg.linear_velocity.linear.x
        currenty=currenty+msg.linear_velocity.linear.y
        currentz=currentz+msg.linear_velocity.linear.z
        y=Float32MultiArray()
        y.data=[float(currentx),float(currenty),float(currentz)]
        self.publisher1.publish(y)
        self.get_logger().info(f'Publishing coordinates{y.data[0]},{y.data[1]},{y.data[2]}')
        if(math.sqrt(math.pow(msg.linear_velocity.linear.x,2)+math.pow(msg.linear_velocity.linear.y,2)+math.pow(msg.linear_velocity.linear.z,2))>3):
            z=String()
            z.data='Warning High Speed'
            self.publisher2.publish(z)
            self.get_logger().info(f'Publishing:{z.data}')
def main(args=None):
    rclpy.init(args=args)
    position_updater=coordinateupdater()
    rclpy.spin(position_updater)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
            