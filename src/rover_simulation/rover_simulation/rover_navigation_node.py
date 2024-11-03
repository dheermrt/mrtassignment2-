import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import argparse
import sys

class RoverNavigationNode(Node):
    def __init__(self, start_position, end_goal):
        super().__init__('rover_navigation_node')
        self.subscription = self.create_subscription(Float32MultiArray, '/obstacle_coordinates', self.listener_callback, 10)
        self.publisher = self.create_publisher(String, '/navigation/status', 10)
        self.start_position = start_position  # Starting position as a tuple
        self.end_goal = end_goal  # End goal as a tuple
        self.steps = 0

    def listener_callback(self, msg):
        obstacle_coords = list(msg.data)
        obstacles = [(obstacle_coords[i], obstacle_coords[i + 1]) for i in range(0, len(obstacle_coords), 2)]
        
        if self.start_position != self.end_goal:
            self.steps += 1
            self.start_position = self.move_towards_goal(self.start_position)

        self.publisher.publish(String(data=f"{self.start_position[0]},{self.start_position[1]}"))
        
        if self.start_position == self.end_goal:
            self.publisher.publish(String(data=f"Goal Reached! {self.steps} Steps"))

    def move_towards_goal(self, current):
        if current[0] < self.end_goal[0]:
            current = (current[0] + 1, current[1])
        elif current[0] > self.end_goal[0]:
            current = (current[0] - 1, current[1])
        if current[1] < self.end_goal[1]:
            current = (current[0], current[1] + 1)
        elif current[1] > self.end_goal[1]:
            current = (current[0], current[1] - 1)
        return current

def main(args=None):
    parser = argparse.ArgumentParser(description='Rover Navigation Node')
    parser.add_argument('--start_position', type=str, default='0,0', help='Starting position in format "x,y"')
    parser.add_argument('--end_goal', type=str, default='9,9', help='End goal in format "x,y"')
    args = parser.parse_args()

    start_position = tuple(map(int, args.start_position.split(',')))
    end_goal = tuple(map(int, args.end_goal.split(',')))

    rclpy.init(args=sys.argv)  
    node = RoverNavigationNode(start_position, end_goal)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
