import sys 
import rclpy 
from std_msgs.msg import String 
from std_msgs.msg import Float32MultiArray
from rclpy.node import Node 
import ast
class RoverNavigate(Node):
    def __init__(self):
        super().__init__('rover_navigate')
        start_param=sys.argv[1]
        target_param=sys.argv[2]
        self.start=ast.literal_eval(start_param)
        self.target=ast.literal_eval(target_param)
        self.current_x=self.start[0]
        self.current_y=self.start[1]
        print(self.start)
        self.steps=0
        self.gridparameters=[]
        self.publisher1=self.create_publisher(String,'status',10)
        self.publisher2=self.create_publisher(Float32MultiArray,'/navigation/status',10)
        self.subscription2=self.create_subscription(Float32MultiArray,'gridparameters',self.define_parameter,10)
        self.subscription=self.create_subscription(Float32MultiArray,'/obstacle_coordinates',self.navigate,10)
        
    print('Hello World 1')
    def define_parameter(self,grid_parameter):
        self.gridparameters=[int(grid_parameter.data[0]),int(grid_parameter.data[1])]
        self.get_logger().info(f'Publishing {self.gridparameters}')
         
         
         
         

    def navigate(self,obstacles_publish):
        obstacle_coordinates=[]
        self.get_logger().info(f'P:{obstacles_publish[0],obstacles_publish[1]}')
        for i in range(0,len(obstacles_publish.data)):
            t=[obstacles_publish.data[i],obstacles_publish.data[i+1]]
            obstacle_coordinates.append(t)
            i=i+2
        print(obstacle_coordinates)
        moves=[(1,0),(0,1),(1,1),(0,-1),(1,-1),(-1,1),(-1,0),(-1,-1)]
        while(self.current_x!=self.target[0] or self.current_y != self.target[1]): 
         c=0
         for i in moves:
            newpos=[self.current_x+i[0],self.current_y+i[1]]
            if(0<=newpos[0]<self.grid_parameters[0] and 0<=newpos[1]<self.grid_parameters[1]):
                if(newpos not in obstacle_coordinates):
                    self.steps=self.steps+1
                    self.current_x=newpos[0]
                    self.current_y=newpos[1]
                    c=1
                    break
         t=Float32MultiArray()
         t.data=[float(self.current_x),float(self.current_y),self.steps]
         self.publisher2.publish(t)
         self.get_logger().info(f'x coord{t.data[0]},y coord{t.data[1]},steps taken{t.data[2]}')
         if(c==0):
            s=String()
            s.data='No path available'
            self.publisher1.publish(s)
            self.get_logger().info(s.data)
            break

        if(self.current_x==self.target[0] and self.current_y==self.target[1]):
            w=String()
            w.data='Collection Successful'
            self.publisher1.publish(w)
            self.get_logger().info(w.data)
def main(args=None):
    rclpy.init(args=args)
    rover_navigate=RoverNavigate()
    rclpy.spin(rover_navigate)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
               



