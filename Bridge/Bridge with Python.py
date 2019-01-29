import rhinoscriptsyntax as rs
from System.Drawing import Color

#Disable redraw
rs.EnableRedraw(False)

#Inputs
L = 10
W = 5
Ndiv = 10 #numbers of divs for structure
Th = 0.5 #stiffners
path = rs.AddLine([0,0,0], [0,0,-Th])
Amp = 0.5 #Amplitude for parabola points
r1 = 0.1

#Define Layers
rs.AddLayer("Beams", Color.Red)
rs.AddLayer("Surface", Color.Blue)
rs.AddLayer("Points", Color.Green)
rs.AddLayer("Columns", Color.Cyan)
rs.AddLayer("Diagonals", Color.Green)
rs.AddLayer("Top pipe", Color.Green)

#Initialize list

Points1 = []
Points2 = []
Points3 = []

##########################################################################
############### Geometric Operations
##########################################################################

#First line of the base

p1 = (-1*L, 0, 0)
p2 = (L,0,0)
L1 = rs.AddLine(p1, p2)
Points1 = rs.DivideCurve(L1, Ndiv, False)

#Second line of the base

p1 = (-1*L, W, 0)
p2 = (L,W,0)
L2 = rs.AddLine(p1, p2)
Points2 = rs.DivideCurve(L2, Ndiv, False)

#Stiffners of the base

rs.CurrentLayer("Beams")

for i in range(Ndiv + 1):
    A_line = rs.AddLine(Points1[i], Points2[i])
    rs.ExtrudeCurve(A_line, path)
    rs.DeleteObject(A_line)
    
#Platform of the base
rs.CurrentLayer("Surface")
rs.AddLoftSrf([L1, L2])

#Definition of parabola points
rs.CurrentLayer("Points")
for i in range(Ndiv + 1):
    x = Points1[i][0]
    P = [x, 0, Amp*(x-L)*(x + L)*(-1/10)]
    Points3.append(rs.AddPoint(P))
    
#Vertical lines btw Points1(base) and Points3 (Points form parabola)
rs.CurrentLayer("Columns")
for i in range(1, Ndiv):
    A_line = rs.AddLine(Points1[i], Points3[i])
    pipe = rs.AddPipe(A_line, 0, r1,blend_type=0, cap=0, fit=False)
    rs.DeleteObject(A_line)
    rs.CopyObject(pipe, (0,W,0))

rs.DeleteObject(path)

#Diagonal stiffeners btw Points1(base) and Points3(Parabola)
rs.CurrentLayer("Diagonals")
for i in range(Ndiv-1):
    A_line = rs.AddLine(Points1[i], Points3[i+1])
    pipe = rs.AddPipe(A_line, 0, r1,blend_type=0, cap=0, fit=False)
    rs.DeleteObject(A_line)
    rs.CopyObject(pipe, (0,W,0))
    
#Top pipes of the bridge
rs.CurrentLayer("Diagonals")
A_line = rs.AddInterpCurve(Points3, degree=3, knotstyle=0, start_tangent=None, end_tangent=None)
pipe = rs.AddPipe(A_line, 0, r1,blend_type=0, cap=0, fit=False)
rs.DeleteObject(A_line)
rs.CopyObject(pipe, (0,W,0))

#Finish
rs.EnableRedraw(True)
rs.CurrentLayer("Default")
rs.ZoomExtents()

print("Program succesful")