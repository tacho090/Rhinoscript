#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################
#For this script to work, create a closed curve on top of a surface, #
#similar to what is shown in example.jpg inside this folder#
############################

import rhinoscriptsyntax as rs
def main():
    surface_id = rs.GetObject("Select a surface to sample", 8, True)#select surface
    if not surface_id: return #if not surface, it will not continue
    curve_id = rs.GetObject("Select a curve to measure", 4, True, True)#select curve
    if not curve_id: return #if not curve, it will not continue
    points = rs.DivideCurve(curve_id, 500) #divide curve in 500 Segments
    rs.EnableRedraw(False)
    for point in points: evaluatedeviation(surface_id, 5.0, point)#calls evaluatedeviation function
    rs.EnableRedraw(True)
def evaluatedeviation( surface_id, threshold, sample ):
    r2point = rs.SurfaceClosestPoint(surface_id, sample)#Returns the UV parameter of the point on a surface that is closest to a test point.
    if not r2point: return
    r3point = rs.EvaluateSurface(surface_id, r2point[0], r2point[1])#evaluates the surface with UV parameters(U=[0] and v[1])
    if not r3point: return
    deviation = rs.Distance(r3point, sample)#sample refers to the previous point
    if deviation<=threshold: return#if deviation is less than threshold do nothing
    rs.AddPoint(sample)#if deviation is more than threshold add point
    rs.AddLine(sample, r3point)#if deviation is more than threshold add line
if __name__=="__main__":
    main()