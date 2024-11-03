from marsservices.srv import Target
import rclpy 
from rclpy.node import Node
class AcceptTarget(Node):
    def __init__(self):
        super().__init__('accept_target')
        self.srv=self.create_service(Target,'target',self.enter_target)
    def enter_target(self,request,response):
        response.success=True
        self.get_logger().info(f'Incoming request{request.target_x},{request.target_y}')
        return response
def main(args=None):
    rclpy.init(args=args)
    accept_target=AcceptTarget()
    rclpy.spin(accept_target)
    rclpy.shutdown()
if __name__ == '__main__':
    main()