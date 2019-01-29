#imports rhinoscriptsyntax to Python Editor
import rhinoscriptsyntax as rs

#Import colors
from System.Drawing import Color

##################Inputs##################

#get curve from rhino space
crv1 = rs.GetObject("Select First Curve", rs.filter.curve)
crv2 = rs.GetObject("Select Second Curve", rs.filter.curve)

#number of divisions for curve
ndiv = 20

#List definition
pt1 = []
pt2 = []
Lines = []

#Define Layers
rs.AddLayer("PythonCurve", Color.Blue)
rs.AddLayer("PythonSurface", Color.Aquamarine)

##################Geometric Operations##################

#divide curves
pt1 = rs.DivideCurve(crv1, ndiv, True, True)
pt2 = rs.DivideCurve(crv2, ndiv, True, True)

#Open Layer called Python Curve, if it exists it DOES NOT DUPLICATE the layer
rs.CurrentLayer("PythonCurve")
#when range is used, it starts at 0 and ends at number inside ()
for i in range(ndiv + 1):
    #conditional, modulus division
    if i % 2 == 0:
    #add elements to lines
        Lines.append(rs.AddLine(pt1[i], pt2[i]))
    #prints i on every loop
    print i

#Open Layer called PythonSurface, if it exists it DOES NOT DUPLICATE the layer
rs.CurrentLayer("PythonSurface")    
Srf1 = rs.AddLoftSrf(Lines)

#Finish procedure
rs.DeleteObjects(Lines)
rs.CurrentLayer("Default")
print("##########...Procedure complete...##########")