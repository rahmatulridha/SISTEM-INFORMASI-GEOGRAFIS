import shapefile
yy = shapefile.Reader("D:/countries/rahma.shp")
shapes = yy.shapes()
print len (shapes)