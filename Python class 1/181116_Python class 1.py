import rhinoscriptsyntax as rs

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

##################Geometric Operations##################

#divide curves
pt1 = rs.DivideCurve(crv1, ndiv, True, True)
pt2 = rs.DivideCurve(crv2, ndiv, True, True)

#when range is used, it starts at 0 and ends at number inside ()
for i in range(ndiv + 1):
    #add elements to lines
    Lines.append(rs.AddLine(pt1[i], pt2[i]))
    #prints i on every loop
    print i
    
Srf1 = rs.AddLoftSrf(Lines)