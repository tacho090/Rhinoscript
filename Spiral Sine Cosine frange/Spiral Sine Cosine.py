import rhinoscriptsyntax as rs
from math import sin, cos

#disable redraw on rhino space
rs.EnableRedraw(False)
#draws a natural sunflower geometry
#starts a loop with float numbers(frange)
for t in rs.frange (100.5,500.25, 1.5):
    p = [t*sin(5*t), t*cos(5*t), t]
    rs.AddPoint(p)
    print (p)

#Finish
#enable redraw on rhino space
rs.EnableRedraw(True)    
print("#######Process finished#######")