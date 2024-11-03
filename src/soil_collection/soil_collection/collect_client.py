import sys 
from marsservices.srv import Target 
import rclpy 
from rclpy.node import Node 
class InputTarget(Node):
    def __init__(self):
        super().__init__('input_target')
        self.cli=self.create_client(Target,'target')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting')
        self.req=Target.Request()
    def send_request(self,target_x,target_y):
        self.req.target_x=float(target_x)
        self.req.target_y=float(target_y)
        self.future=self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self,self.future)
        return self.future.result()
def main(args=None):
    rclpy.init(args=None)
    target_input=sys.argv[1]
    try:
        coordinates=eval(target_input)
        for i in coordinates:
            print(i)
    except Exception as e:
        print(f'Error parsing{e}')
        sys.exit(1)
    input_target=InputTarget()
    for(x,y) in coordinates:
        response=input_target.send_request(float(x),float(y))
        if response:
            input_target.get_logger().info(f'input was{float(x)},{float(y)}')
    rclpy.shutdown()
     
if __name__ == '__main__':
    main()