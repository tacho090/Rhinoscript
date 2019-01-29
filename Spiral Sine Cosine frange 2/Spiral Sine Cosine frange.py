import rhinoscriptsyntax as rs
from math import sin, cos

#disable redraw on rhino space
rs.EnableRedraw(False)
#draws a natural sunflower geometry
#starts a loop with float numbers(frange)
for t in rs.frange (500.50,1000.25, 1.0):
    p = [t*sin(5*t), t*cos(5*t), t]
    rs.AddPoint(p)
    

#Finish
#enable redraw on rhino space
rs.EnableRedraw(True)

#zoom extents of drawn geometry
rs.ZoomExtents()    
print("#######Process finished#######")