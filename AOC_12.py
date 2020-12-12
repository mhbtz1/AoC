import math
import numpy as np
a = [i.split('\n') for i in open("AOC_12.txt","r").readlines()]
a = [i[0:len(i)-1] for i in a]
a[len(a)-1]=['F35']
print(a)
DIR = 'E'
ANGLE = 0
pt_cur = (10,1) #for pt. 2, this is the waypoint


#the basis for part 2 is an observation in linear algebra for rotating points in n-dimensions for n=2
#part 1 is just trig and implementation

pt_ship = (0,0)
for dire in a:
    dir_x = int(dire[0][1:])*round(np.cos(ANGLE))
    dir_y = int(dire[0][1:])*round(np.sin(ANGLE))
    val = int(dire[0][1:])
    print(pt_ship)
    print(pt_cur)
    if(dire[0][0]=='F'):
        x,y=pt_cur
        aq,bq = pt_ship
        #pt_ship = (aq+dir_x*x, bq+dir_y*y)
        pt_ship = (aq + x*val, bq + y*val)
    if(dire[0][0]=='N'):
        x,y=pt_cur
        pt_cur=(x,y+val)
    if(dire[0][0]=='S'):
        x,y=pt_cur
        pt_cur=(x,y-val)
    if(dire[0][0]=='E'):
        x,y=pt_cur
        pt_cur=( x+val,y)
    if(dire[0][0]=='W'):
        x,y=pt_cur
        pt_cur=(x-val, y)
    if(dire[0][0]=='L'):
        ANGLE += np.deg2rad(val)
        aq,bq=pt_cur
        v1 = (aq*np.cos(np.deg2rad(val))) - (bq*np.sin(np.deg2rad(val)))
        v2 = (aq*np.sin(np.deg2rad(val))) + (bq*np.cos(np.deg2rad(val)))
        pt_cur = (round(v1),round(v2))
    if(dire[0][0]=='R'):
        ANGLE -= np.deg2rad(val)
        aq,bq=pt_cur
        v_1 = aq*np.cos(-(np.deg2rad(val))) - bq*np.sin(-(np.deg2rad(val)))
        v_2 = aq*np.sin(-(np.deg2rad(val))) + bq*np.cos(-(np.deg2rad(val)))
        pt_cur = ( round(v_1),round(v_2) )


    #num += 1
a,b=pt_ship
print(pt_ship)
print( abs(a)+abs(b))
