import rclpy
from rclpy.node import Node 
from mars.msg import RoverOdometry

import random 

class VelocityPublish(Node):
    def __init__(self):
        super().__init__('velocity_publish')
        self.publisher=self.create_publisher(RoverOdometry,'motiondata',10)
        self.timer =self.create_timer(1,self.timer_callback)
    def timer_callback(self):
        msg=RoverOdometry()
        msg.rover_id= 1
        msg.orientation= 3.00
        msg.angular_velocity= float(10*(random.random()))
        msg.linear_velocity.linear.x=float(10*random.random())
        msg.linear_velocity.linear.y=float(10*random.random())
        msg.linear_velocity.linear.z=float(10*random.random())
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing{msg.rover_id,msg.orientation,msg.angular_velocity} \n vx={msg.linear_velocity.linear.x}')
def main(args=None):
    rclpy.init(args=args)
    velocity_publish = VelocityPublish()
    rclpy.spin(velocity_publish)
    rclpy.shutdown()
if __name__ == '__main__':
    main()

    


