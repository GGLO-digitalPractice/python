import clr
import math

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

elev = []
angle_ = []
#view = []
axis = []

#for i,j,k in zip(IN[0],IN[1],IN[2]):
for i,j,m in zip(IN[0],IN[1],IN[3]):
    elev.append(UnwrapElement(i))
    angle_.append(math.radians(j))
    #view.append(UnwrapElement(k))
    axis.append(m.ToRevitType())

#elev = UnwrapElement(IN[0])
#angle_ = math.radians(IN[1])
view = UnwrapElement(IN[2])


TransactionManager.Instance.EnsureInTransaction(doc)
c = 0
for e in elev:
#    bbox = e.BoundingBox[view[c]]
#    diag = Line.CreateBound(bbox.Min,bbox.Max)
#    p1 = diag.Evaluate(0.5, True)
#    p2 = XYZ(p1.X, p1.Y,p1.Z+1)
#    axis_ = Line.CreateBound(p1, p2)
    Autodesk.Revit.DB.ElementTransformUtils.RotateElement(doc, e.Id, axis[c], angle_[c])
    c+=1
	
TransactionManager.Instance.TransactionTaskDone()

OUT = elev