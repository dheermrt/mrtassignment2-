import sys
import rclpy 
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import ast
class ObstacleAvoid(Node):
    def __init__(self):
        super().__init__('obstacle_avoid')
        grid_param=sys.argv[1]
          
        self.grid=ast.literal_eval(grid_param)
        print(self.grid)
        self.publisher =self.create_publisher(Float32MultiArray,'/obstacle_coordinates',10)
        self.publisher1=self.create_publisher(Float32MultiArray,'gridparameters',10)
        self.publish()
    def publish(self):
        obstacles=[]
        for i in range (0,len(self.grid)):
            for j in range(0,len(self.grid[i])):
                if self.grid[i][j]==1:
                    obstacles.append((float(j),float(i)))
        obstacles_publish=Float32MultiArray()
        obstacles_publish.data=[t for coord in obstacles for t in coord]
        self.publisher.publish(obstacles_publish)
        grid_parameter=Float32MultiArray()
        grid_parameter.data=[float(len(self.grid[0])),float(len(self.grid))]
        self.publisher1.publish(grid_parameter)
        self.get_logger().info(f'Publishing{obstacles_publish.data}')
        self.get_logger().info(f'Grid parameters{grid_parameter.data[0],grid_parameter.data[1]}')
def main(args=None):
    rclpy.init(args=args)
    obstacle_avoid=ObstacleAvoid()
    rclpy.spin(obstacle_avoid)
    rclpy.shutdown()
if __name__ == '__main__':
    main()

        