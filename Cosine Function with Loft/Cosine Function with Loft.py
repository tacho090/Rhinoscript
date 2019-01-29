import rhinoscriptsyntax as rs
from math import cos, sin
from System.Drawing import Color

#inputs
np = 50
offset = 30
c_x = 0.2
c_z = 0.3

#List definition
Crvs = []

#if the function is called the inputs are passed as arguments to the function
def createcurve(index, offset, np, c_x, c_z):
    #List definition
    pts = []
    
    #Layer creation
    rs.AddLayer("PythonCurve", Color.Blue)
    rs.AddLayer("PythonCosineCurve", Color.Aquamarine)
    rs.AddLayer("CosineCurve", Color.Red)
    rs.AddLayer("CosineSurface", Color.AliceBlue)
    
    ##################Geometric Operations##################
    
    if index%2 == 0:
        f = sin
    else:
        f = cos
    
    
    rs.CurrentLayer("CosineCurve")
    
    for i in range(np):
        #x = 50 + i*c_x
        x = i*c_x
        y = 0 + offset
        z = f(i*c_z)
        
        pts.append([x,y,z])
        
    #rs.addInterpCurve(pts)
    return rs.AddInterpCurve(pts, 3,0)
    
#A loop for creating a number of curves
for n in range(40):
    #it starts at 0
    crv = createcurve(n, n, np, c_x, c_z)
    Crvs.append(crv)
    
#Surface definition
rs.CurrentLayer("CosineSurface")
rs.AddLoftSrf(Crvs)

#Delete created curves
rs.DeleteObjects(Crvs)

print("#########Process finished#########")