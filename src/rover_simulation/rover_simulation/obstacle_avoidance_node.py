import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String
import argparse

class ObstacleAvoidanceNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance_node')
        self.publisher = self.create_publisher(Float32MultiArray, '/obstacle_coordinates', 10)
        self.create_subscription(String, '/navigation/status', self.listener_callback, 10)
        self.current_position = (0, 0)   
        self.grid = self.parse_arguments()

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Obstacle Avoidance Node')
        parser.add_argument('--grid', type=str, required=True, help='Grid matrix in format "0,0,1,...,1"')
        args = parser.parse_args()
        grid_flat = list(map(int, args.grid.split(',')))
        grid_size = int(len(grid_flat) ** 0.5)
        grid = []
        for i in range(grid_size):
            grid.append(grid_flat[i * grid_size:(i + 1) * grid_size])
        return grid

    def listener_callback(self, msg):
        self.current_position = tuple(map(int, msg.data.split(',')))
        self.publish_obstacle_coordinates()

    def publish_obstacle_coordinates(self):
        obstacles = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 1:
                    obstacles.append((i - self.current_position[0], j - self.current_position[1]))
        obstacle_msg = Float32MultiArray(data=[coord for pair in obstacles for coord in pair])
        self.publisher.publish(obstacle_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidanceNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
