def Polygon_C(Center, R, N):
    import rhinoscriptsyntax as rs
    from math import tan, pi
    
    #List Definition
    vertex = []
    Erase = []
    
    #####################################################################
    ########    Geometric Operations
    #####################################################################
    
    pt = rs.AddPoint([Center[0],Center[1] + R, Center[2]])
    
    #angle in degrees divided by the number of sides
    Alf = 2.*pi/N
    #angle in degrees divided by the number of sides
    Alfa = 360./N
    
    #you have to add a vector in the x direction which is the radius 
    #multiplied by tangent of the angle divided by 2
    pt2 = rs.PointAdd(pt,(R*tan(Alfa/2), 0, 0))
    
    #Draw point on rhinospace
    pt2 =rs.AddPoint(pt2)
    
    #Loop for the rest of the vertex
    for i in range(N+1):
        p = rs.RotateObject(pt2, Center, i*Alfa, axis=None, copy=True)
        vertex.append(p)
        
    #Define Polyline
    rs.AddPolyline(vertex)
    
    #Finish
    Erase = [pt, pt2]
    
    #We extended our existing list, is equivalent to add a list to another list 
    vertex.extend(Erase)
    
    #Delete points at vertexes
    rs.DeleteObjects(vertex)
    
    print("Operation complete")
