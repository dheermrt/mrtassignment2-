import rclpy 
from marsservices.srv import Target 
from rclpy.node import Node
from std_msgs.msg import String
class CollectStatus(Node):
    def __init__(self,grid):
        super().__init__('collect_status')
        self.srv=self.create_service(Target,'target',self.collect_target)
        self.publisher=self.create_publisher(String,'/soil_collection/status',10)
        self.grid=grid
        self.attempts=[]
        self.current_x=0
        self.current_y=0
       
        
               
    def collect_target(self,request,response):
        self.current_x,self.current_y=0,0
        x,y=int(request.target_x),int(request.target_y)
        self.get_logger().info(f'Target coordinates are:{x,y}')
         
        while(self.current_x !=x or self.current_y !=y):
            moves=[(1,0),(0,1),(1,1),(0,-1),(1,-1),(-1,1),(-1,0),(-1,-1)]
             
            for i in moves:
              newpos = [ self.current_x+i[0],self.current_y+i[1]]
              print(newpos[0],newpos[1])
              if(0<=newpos[0]<len(self.grid[0]) and 0<=newpos[1]<len(self.grid)):
                if (self.grid[newpos[1]][newpos[0]] != 1.0):
                 self.current_x=newpos[0]
                 self.current_y=newpos[1]
                 break
                  
                      
             
                 
                
                 
        print('Loop exited')
             
        if( self.current_x == x and self.current_y == y):
            q=String()
            q.data='Collection Successful'
            self.publisher.publish(q)
            self.get_logger().info(q.data)
            self.attempts.append(1)
        else:
            w=String()
            w.data='Collection unsuccessful'
            self.publisher.publish(w)
            self.get_logger().info(w.data) 
            self.attempts.append(0) 
        response.success=True 
        return response



       
     
        
       


  
def main(args=None):
    rclpy.init(args=args)
    t =input('Enter the grid matrix as string')
    grid=t.splitlines()
    collect_status=CollectStatus(grid)
    rclpy.spin(collect_status)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
