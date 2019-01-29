import rhinoscriptsyntax as rs
from math import cos
from System.Drawing import Color

#inputs
np = 100
offset = 30

#if the function is called the inputs are passed as arguments to the function
def createcurve(offset, np):
    #List definition
    pts = []
    
    #Layer creation
    rs.AddLayer("PythonCurve", Color.Blue)
    rs.AddLayer("PythonCosineCurve", Color.Aquamarine)
    rs.AddLayer("CosineCurve", Color.Red)
    
    ##################Geometric Operations##################
    
    #rs.CurrentLayer("PythonCurve")
    rs.CurrentLayer("CosineCurve")
    
    for i in range(np):
        x = i
        y = 0 + offset-20
        z = cos(i+1)
        
        pts.append([x,y,z])
        
    #rs.addInterpCurve(pts)
    rs.AddInterpCurve(pts, 3,0)
    
#A loop for creating a number of curves
for n in range(40):
    #it starts at 0
    createcurve(n*0.5, np)
    
print("#########Process finished#########")