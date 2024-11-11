import math
import numpy as np
import numpy.linalg as la


class trajectory_generator(object):
    def __init__(self):
        pass


    def hover_test(self, x_offset):
        ref_x = 0
        ref_y = 0.6
        ref_z = 0.2
        ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
        msg = "hovering test..."
        return (ref_pos,msg)
    

    def low_alt_rectangle(self, x_offset, abs_time):
        if abs_time < 3:
            ref_x = 0
            ref_y = 0.6
            ref_z = 0.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 3 <= abs_time < 7:
            ref_x = 0
            ref_y = 0.9
            ref_z = 0.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 7 <= abs_time < 11:
            ref_x = 0
            ref_y = 1.2
            ref_z = 0.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..." 
        elif 11 <= abs_time < 15:
            ref_x = 0.5
            ref_y = 1.2
            ref_z = 0.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 15 <= abs_time < 19:
            ref_x = 0.5
            ref_y = 0.9
            ref_z = 0.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 19 <= abs_time < 23:
            ref_x = 0.5
            ref_y = 0.6
            ref_z = 0.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 23 <= abs_time < 27:
            ref_x = 0
            ref_y = 0.6
            ref_z = 0.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 27 <= abs_time:
            ref_x = 0
            ref_y = 0.6
            ref_z = 0.02
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "traj ended..."

        return (ref_pos,msg)
    

    def simple_rectangle(self, x_offset, abs_time):
        if abs_time < 3:
            ref_x = 0
            ref_y = 0.6
            ref_z = 1.0
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 3 <= abs_time < 7:
            ref_x = 0
            ref_y = 0.9
            ref_z = 1.0
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 7 <= abs_time < 11:
            ref_x = 0
            ref_y = 1.2
            ref_z = 1.0
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..." 
        elif 11 <= abs_time < 15:
            ref_x = 0.5
            ref_y = 1.2
            ref_z = 1.0
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 15 <= abs_time < 19:
            ref_x = 0.5
            ref_y = 0.9
            ref_z = 1.0
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 19 <= abs_time < 23:
            ref_x = 0.5
            ref_y = 0.6
            ref_z = 1.0
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 23 <= abs_time < 27:
            ref_x = 0
            ref_y = 0.6
            ref_z = 0.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 27 <= abs_time:
            ref_x = 0
            ref_y = 0.6
            ref_z = 0.02
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "traj ended..."

        return (ref_pos,msg)
    

    def elevated_rectangle(self, x_offset, abs_time):
        if abs_time < 3:
            ref_x = 0
            ref_y = 0.6
            ref_z = 0.3
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 3 <= abs_time < 7:
            ref_x = 0
            ref_y = 0.9
            ref_z = 0.7
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 7 <= abs_time < 11:
            ref_x = 0
            ref_y = 1.2
            ref_z = 1.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..." 
        elif 11 <= abs_time < 15:
            ref_x = 0.5
            ref_y = 1.2
            ref_z = 1.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 15 <= abs_time < 19:
            ref_x = 0.5
            ref_y = 0.9
            ref_z = 0.7
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 19 <= abs_time < 23:
            ref_x = 0.5
            ref_y = 0.6
            ref_z = 0.3
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 23 <= abs_time < 27:
            ref_x = 0
            ref_y = 0.6
            ref_z = 0.2
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "still flying..."
        elif 27 <= abs_time:
            ref_x = 0
            ref_y = 0.6
            ref_z = 0.02
            ref_pos = np.array([ref_x+x_offset, ref_y, ref_z])
            msg = "traj ended..."

        return (ref_pos,msg)
    
       
    def simple_circle(self, x_offset, radius, count):
        num_points = 3142
        theta = np.linspace(0, 2*np.pi, num_points) # 3142 pts for 0.1m/s

        # the radius of the circle
        r = np.sqrt(radius)

        # compute x and y, starts from bottom facing positive x
        x = r*np.cos(theta) + x_offset 
        y = r*np.sin(theta) + 0.8
        
        if count >= num_points:
            ref_x = x[-1]
            ref_y = y[-1]
            ref_z = 0.02
            msg = "traj ended..."
        else:
            ref_x = x[count]
            ref_y = y[count]
            ref_z = 0.5
            msg = "still flying..."

        ref_pos = np.array([ref_x, ref_y, ref_z])
        
        return (ref_pos,msg)


    def elevated_circle(self, x_offset, radius, count):
        num_points = 3142
        theta = np.linspace(0, 2*np.pi, num_points) # 3142 pts for 0.1m/s

        # the radius of the circle
        r = np.sqrt(radius)

        # compute x and y, starts from bottom facing positive x
        x = r*np.cos(theta) + x_offset 
        y = r*np.sin(theta) + 0.8
        z = y

        if count >= num_points:
            ref_x = x[-1]
            ref_y = y[-1]
            ref_z = 0.02
            msg = "traj ended..."
        else:
            ref_x = x[count]
            ref_y = y[count]
            ref_z = z[count]
            msg = "still flying..."

        ref_pos = np.array([ref_x, ref_y, ref_z])

        return (ref_pos,msg)


    