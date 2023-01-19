import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

subDir = []

geo = "Autodesk.DesignScript.Geometry"

for i in dir(geo):
	dir_str = getattr(geo, i)
	subDir.append(dir(dir_str))
# Assign your output to the OUT variable.
OUT = dir(geo), subDir