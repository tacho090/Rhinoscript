import rhinoscriptsyntax as rs
from Module_Example import Polygon_I
from System.Drawing import Color

print("Module imported succesfully")

#Define Lists
Points1 = []
Points2 = []

#Define Layers
rs.AddLayer("Legs", Color.Red)
rs.AddLayer("Tabletop", Color.Blue)

#Inputs
H = 4.
R = 2.
N = 6 #number of sides
radius_pipes = 0.1
Legs = []
offset_dist = .5 #offset for the top polygon(table top)
erase = [] 

######################################################################
##################Geometric Operations
######################################################################

#Disable redraw
rs.EnableRedraw(False)

#Initial Polygon
Cen_base = (0,0,0)

#Height of end polygon
Cen_top = (0,0,H)

#Extrude path
extrude_path = rs.AddLine(Cen_base, [0,0,0.2])

Poly_base = Polygon_I(Cen_base,R, N )
Poly_top = rs.CopyObject(Poly_base, (0,0,H))

#Returns Curve Control Points
Points1 = rs.CurvePoints(Poly_base)
Points2 = rs.CurvePoints(Poly_top)

#Construct the legs

rs.CurrentLayer("Legs")

#loop for lines which will be legs
for i in range(N):
    A_lines = rs.AddLine(Points1[i], Points2[i]) #lines for the pipes
    
    #Add pipes
    pipe = rs.AddPipe(A_lines, 0, radius_pipes, blend_type=0, cap=1, fit=False)
    
    #Append each pipe to Legs
    Legs.append(pipe)
    
#rs.DeleteObjects([A_lines, Poly_base, Poly_top])

#Create group
rs.AddGroup("Legs")
rs.AddObjectsToGroup(Legs, "Legs")

#Construct the table top, draw offset curve
offset_crv = rs.OffsetCurve(Poly_top, Cen_top, -(offset_dist), normal=None, style=1)

rs.CurrentLayer("Tabletop")
#extrude Offset Curve
extruded_crv = rs.ExtrudeCurve(offset_crv, extrude_path)

#cap Extruded shape
closed_polysrf = rs.CapPlanarHoles(extruded_crv)


#Delete objects
erase = [A_lines, Poly_base, Poly_top, offset_crv]
rs.DeleteObjects(erase)

#Redraw geometry
rs.EnableRedraw(True)

#zoom extents of drawn geometry
rs.ZoomExtents()  

rs.CurrentLayer("Default")


print("***************Program succesful***************")